from django.conf import settings

from core.models import SiteSettings

NAVIGATION = [
    {"label": "Projects", "href": "/projects"},
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
    return {
        "site": SiteSettings.load(),
        "navigation": navigation,
        "site_url": settings.SITE_URL,
    }
