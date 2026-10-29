"""Custom landing pages whose every text, image and list is edited in the admin.

Each page has a module in projects/landing_pages/ describing its content slots and their starting
content. seed() turns those into LandingPage rows (it runs from a migration, so `migrate` is enough
on any machine); context() hands them to the page's template as:

    t.<key>              a text; render with |em to turn *stars* into italics
    imgs.<key>.image     a single picture, with imgs.<key>.alt; render with |src:<width>
    lists.<key>          the published items of a list, in order
"""

from pathlib import Path

from django.apps import apps as django_apps
from django.conf import settings
from django.core.files import File
from django.core.files.storage import default_storage

from projects.landing_pages import billionaire, cullinan, jacob, trump

PAGES = {module.SLUG: module for module in (jacob, cullinan, trump, billionaire)}


def list_choices(slug=None):
    """(key, name) of the lists on one page, or on every page."""
    modules = [PAGES[slug]] if slug in PAGES else PAGES.values()
    choices = {}
    for module in modules:
        for key, (name, _help) in module.LISTS.items():
            choices.setdefault(key, name)
    return sorted(choices.items(), key=lambda choice: choice[1])


def list_help(slug):
    module = PAGES.get(slug)
    return [(name, help_text) for name, help_text in module.LISTS.values()] if module else []


def _copy_static(module, filename):
    """Copy a starting image from static/ into the media folder, where the admin can replace it."""
    if not filename:
        return ""
    name = f"landing/{module.SLUG}/{Path(filename).name}"
    if not default_storage.exists(name):
        with open(Path(settings.BASE_DIR) / "static" / module.STATIC_DIR / filename, "rb") as source:
            name = default_storage.save(name, File(source))
    return name


def seed(apps=None):
    """Create any missing page, text and image. Lists are filled only when their page is new,
    so items the content team deleted do not come back. Never overwrites edited content."""
    get_model = (apps or django_apps).get_model
    LandingPage = get_model("projects", "LandingPage")
    LandingText = get_model("projects", "LandingText")
    LandingImage = get_model("projects", "LandingImage")
    LandingItem = get_model("projects", "LandingItem")

    for module in PAGES.values():
        seo = dict(module.SEO)
        share_image = _copy_static(module, seo.pop("share_image", ""))
        page, created = LandingPage.objects.get_or_create(
            slug=module.SLUG, defaults={"name": module.NAME, "share_image": share_image, **seo}
        )
        for order, (section, key, label, value) in enumerate(module.TEXTS):
            text, new = LandingText.objects.get_or_create(
                page=page, key=key, defaults={"section": section, "label": label, "value": value, "order": order}
            )
            if not new:  # Sections, labels and order describe the template, so they follow the code.
                LandingText.objects.filter(pk=text.pk).update(section=section, label=label, order=order)
        for order, (section, key, label, filename, alt) in enumerate(module.IMAGES):
            image, new = LandingImage.objects.get_or_create(
                page=page,
                key=key,
                defaults={
                    "section": section,
                    "label": label,
                    "image": _copy_static(module, filename),
                    "alt": alt,
                    "order": order,
                },
            )
            if not new:
                LandingImage.objects.filter(pk=image.pk).update(section=section, label=label, order=order)
        if created:
            for list_key, items in module.ITEMS.items():
                for order, item in enumerate(items):
                    item = dict(item)
                    item["image"] = _copy_static(module, item.get("image", ""))
                    LandingItem.objects.create(page=page, list_key=list_key, order=order, **item)


def context(slug, rera=""):
    """Template context for a landing page, or None when the page has no content in the admin."""
    from projects.models import LandingPage

    page = LandingPage.objects.filter(slug=slug).first()
    if page is None:
        return None

    def fill(value):
        return value.replace("{rera}", rera)

    lists = {}
    for item in page.items.filter(is_published=True):
        item.title, item.text = fill(item.title), fill(item.text)
        lists.setdefault(item.list_key, []).append(item)
    return {
        "landing": page,
        "t": {text.key: fill(text.value) for text in page.texts.all()},
        "imgs": {image.key: image for image in page.images.all()},
        "lists": lists,
    }
