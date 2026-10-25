"""
Image helpers.

- ResizingImageField downsizes very large uploads so the admin team can
  upload camera-sized files without slowing the site down.
- get_renditions() lazily creates WebP copies at a few widths for srcset,
  which is what next/image did for the previous site.
"""

import logging
from io import BytesIO
from pathlib import Path

from django.conf import settings
from django.core.cache import cache
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.db import models
from PIL import Image, ImageOps

logger = logging.getLogger(__name__)

RENDITION_DIR = "renditions"


class ResizingImageField(models.ImageField):
    def save_form_data(self, instance, data):
        if data and hasattr(data, "read") and not isinstance(data, str):
            data = _downsize_upload(data)
        super().save_form_data(instance, data)


def _downsize_upload(upload):
    max_width = settings.IMAGE_MAX_UPLOAD_WIDTH
    try:
        upload.seek(0)
        with Image.open(upload) as image:
            if image.format not in {"JPEG", "PNG", "WEBP"} or image.width <= max_width:
                upload.seek(0)
                return upload
            image = ImageOps.exif_transpose(image)
            ratio = max_width / image.width
            image = image.resize((max_width, round(image.height * ratio)), Image.Resampling.LANCZOS)
            buffer = BytesIO()
            fmt = image.format or "JPEG"
            if fmt == "JPEG" and image.mode != "RGB":
                image = image.convert("RGB")
            image.save(buffer, format=fmt, quality=86, optimize=True)
    except Exception:  # Leave unusual files untouched; Django's own validation still runs.
        logger.exception("Could not downsize uploaded image")
        upload.seek(0)
        return upload
    return ContentFile(buffer.getvalue(), name=Path(upload.name).name)


def get_renditions(field_file):
    """Return [(url, width), ...] WebP renditions, creating any that are missing."""
    if not field_file:
        return []
    cache_key = f"renditions:{field_file.name}"
    cached = cache.get(cache_key)
    if cached is not None:
        return cached
    try:
        width = field_file.width
    except Exception:
        return []

    source = Path(field_file.name)
    renditions = []
    for target in settings.IMAGE_RENDITION_WIDTHS:
        if target >= width:
            continue
        name = f"{RENDITION_DIR}/{source.parent.as_posix()}/{source.stem}-{target}w.webp"
        if not default_storage.exists(name):
            try:
                _create_rendition(field_file, name, target)
            except Exception:
                logger.exception("Could not create rendition %s", name)
                continue
        renditions.append((default_storage.url(name), target))
    cache.set(cache_key, renditions, 60 * 60 * 24)
    return renditions


def _create_rendition(field_file, name, target):
    field_file.open("rb")
    try:
        with Image.open(field_file) as image:
            image = ImageOps.exif_transpose(image)
            ratio = target / image.width
            image = image.resize((target, max(1, round(image.height * ratio))), Image.Resampling.LANCZOS)
            if image.mode not in {"RGB", "RGBA"}:
                image = image.convert("RGBA" if "A" in image.getbands() else "RGB")
            buffer = BytesIO()
            image.save(buffer, format="WEBP", quality=80, method=5)
    finally:
        field_file.close()
    default_storage.save(name, ContentFile(buffer.getvalue()))
