from django.conf import settings

from core.models import Page, SiteSettings
from projects.models import Project

# The Projects dropdown: projects with their own ad landing page, shown while published.
PROJECT_MENU = [
    ("m3m-jacob-co-residences", "M3M Jacob & Co. Residences", "Sector 97 · 3, 4 & 5 BHK"),
    ("m3m-the-cullinan-residential", "M3M The Cullinan", "Sector 94 · 3, 4 & 5 BHK"),
    ("m3m-trump-tower-noida", "M3M Trump Tower Noida", "Sector 94 · 4 & 5 BHK"),
]

NAVIGATION = [
    {"label": "Projects", "href": "/projects", "dropdown": True},
    {"label": "Our Journey", "href": "/our-journey"},
    {"label": "Media", "href": "/media-centre"},
    {"label": "Insights", "href": "/insights"},
    {"label": "Contact Us", "href": "/contact"},
    # Highlighted in gold at the end of the menu: M3M's flagship address.
    {"label": "Billionaire Block", "href": "/billionaire-block", "featured": True},
]


def site(request):
    path = request.path
    navigation = [
        {**item, "active": path == item["href"] or path.startswith(item["href"] + "/")}
        for item in NAVIGATION
    ]
    published = set(
        Project.objects.published().filter(slug__in=[slug for slug, _, _ in PROJECT_MENU]).values_list("slug", flat=True)
    )
    children = [
        {"label": label, "note": note, "href": f"/projects/{slug}"}
        for slug, label, note in PROJECT_MENU
        if slug in published
    ]
    for item in navigation:
        if item.get("dropdown"):
            item["children"] = children
    return {
        "site": SiteSettings.load(),
        "navigation": navigation,
        # Footer links to the legal pages, only once each is published.
        "legal_pages": Page.objects.filter(is_published=True).order_by("slug"),
        "site_url": settings.SITE_URL,
    }
