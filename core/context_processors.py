from django.conf import settings

from core.models import Page, SiteSettings
from projects import landing
from projects.landing_pages import site as site_texts
from projects.models import Project

def _menu(lists, key):
    """A menu list from “Website texts” in the admin, or its starting items if that page is missing."""
    if lists is None:
        return site_texts.ITEMS[key]
    return [{"title": i.title, "subtitle": i.subtitle, "link": i.link, "group": i.group} for i in lists.get(key, [])]


def site(request):
    # The header menu, its Projects dropdown and the shared texts (st.<key>) are edited in the admin
    # under “Website texts” (projects/landing_pages/site.py).
    texts = landing.context(site_texts.SLUG)
    lists = texts["lists"] if texts else None
    path = request.path
    navigation = [
        {
            "label": item["title"],
            "href": item["link"],
            "featured": item["group"] == "featured",
            "dropdown": item["group"] == "dropdown",
            "active": path == item["link"] or path.startswith(item["link"].rstrip("/") + "/"),
        }
        for item in _menu(lists, "menu")
    ]
    published = set(Project.objects.published().values_list("slug", flat=True))
    children = [
        {"label": item["title"], "note": item["subtitle"], "href": item["link"]}
        for item in _menu(lists, "project_menu")
        if not item["link"].startswith("/projects/") or item["link"].rstrip("/").rsplit("/", 1)[-1] in published
    ]
    for item in navigation:
        if item["dropdown"]:
            item["children"] = children
    return {
        "site": SiteSettings.load(),
        "st": texts["t"] if texts else {key: value for _, key, _, value in site_texts.TEXTS},
        "navigation": navigation,
        # Footer links to the legal pages, only once each is published.
        "legal_pages": Page.objects.filter(is_published=True).order_by("slug"),
        "site_url": settings.SITE_URL,
    }
