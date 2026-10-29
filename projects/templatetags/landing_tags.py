import re

from django import template
from django.utils.html import escape
from django.utils.safestring import mark_safe

from core.images import get_renditions

register = template.Library()


@register.filter
def em(value):
    """Escape an admin text and show its *starred* words in italics, as the page headings do."""
    return mark_safe(re.sub(r"\*(.+?)\*", r"<em>\1</em>", escape(value or "")))


@register.filter
def src(field_file, width=1920):
    """URL of the smallest WebP copy at least `width` pixels wide, or of the uploaded file itself."""
    if not field_file:
        return ""
    for url, rendition_width in sorted(get_renditions(field_file), key=lambda rendition: rendition[1]):
        if rendition_width >= int(width):
            return url
    return field_file.url


@register.filter
def unit(value, name):
    """Put a residence name in place of {unit}, e.g. “Unlock {unit} details”."""
    return (value or "").replace("{unit}", str(name))
