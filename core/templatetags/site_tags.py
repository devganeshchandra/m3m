from django import template
from django.utils.html import format_html

from core.images import get_renditions

register = template.Library()


@register.simple_tag
def picture(field_file, sizes="100vw", alt="", css_class="", priority=False, fill=True):
    """Render an <img> with WebP srcset, like next/image did on the old site."""
    if not field_file:
        return ""
    candidates = [f"{url} {width}w" for url, width in get_renditions(field_file)]
    try:
        candidates.append(f"{field_file.url} {field_file.width}w")
    except Exception:
        pass
    classes = " ".join(filter(None, ["img-fill" if fill else "", css_class]))
    loading = "eager" if priority else "lazy"
    fetch_priority = "high" if priority else "auto"
    return format_html(
        '<img alt="{}" class="{}" src="{}" srcset="{}" sizes="{}" loading="{}" fetchpriority="{}" decoding="async">',
        alt,
        classes,
        field_file.url,
        ", ".join(candidates),
        sizes,
        loading,
        fetch_priority,
    )


@register.filter
def pad2(value):
    return f"{int(value):02d}"


@register.filter
def lt(value, other):
    return int(value) < int(other)
