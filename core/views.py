from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.decorators.http import require_GET

from content.models import Insight, JourneyPrinciple, JourneyStat, MediaImage, Milestone, PressItem, Publication, Video
from core.models import FAQ, HeroBanner, HomePage, InnerPage, Page
from projects.models import BillionaireBlockPage, Project

HOME_MEDIA_COUNT = 8  # Fills the homepage gallery grid exactly (3 rows).
HOME_LIST_COUNT = 3


def inner_page(key):
    page = InnerPage.for_key(key)
    if page is None:
        raise Http404("Run `python manage.py seed_content` to create the menu pages.")
    return page


def featured_publications():
    """Publications with at least one visible news item, for the "As featured in" strip."""
    return Publication.objects.filter(items__is_published=True).distinct()


@require_GET
def home(request):
    projects = Project.objects.published()
    press = PressItem.objects.filter(is_published=True).select_related("publication")
    publications = featured_publications()
    images = MediaImage.objects.filter(is_published=True)
    page = HomePage.load()
    context = {
        "page": page,
        "billionaire": BillionaireBlockPage.load(),
        "banners": HeroBanner.objects.filter(is_active=True),
        "projects": Project.objects.for_homepage(HOME_LIST_COUNT),
        "project_total": projects.count(),
        "guided_projects": projects,
        "principles": JourneyPrinciple.objects.filter(is_published=True),
        "stats": JourneyStat.objects.filter(is_published=True),
        "press_items": press[:HOME_LIST_COUNT],
        "press_publications": publications,
        "media_images": images[:HOME_MEDIA_COUNT],
        "insights": Insight.objects.filter(is_published=True)[:HOME_LIST_COUNT],
        # Figures shown beside each section heading, counted from the live content.
        # Company-wide figures from the admin; otherwise counted from the projects on this site.
        "projects_facts": page.projects_fact_list
        or [
            (projects.count(), "Addresses"),
            (projects.filter(is_residential=True).count(), "Residential"),
            (projects.filter(is_commercial=True).count(), "Commercial"),
        ],
        "news_facts": [
            (press.count(), "Stories"),
            (publications.count(), "Publications"),
        ],
        "media_facts": [
            (images.count(), "Images"),
            (images.order_by().values("category").distinct().count(), "Collections"),
        ],
    }
    latest = press.order_by("-published_on").first()
    if latest:
        context["news_facts"].append((latest.published_on.strftime("%b %Y"), "Latest story"))
    videos = Video.objects.filter(is_published=True).count()
    if videos:
        context["media_facts"].append((videos, "Films"))
    return render(request, "home/home.html", context)


@require_GET
def journey(request):
    architecture = MediaImage.objects.filter(is_published=True, category=MediaImage.Category.ARCHITECTURE)
    context = {
        "inner": inner_page(InnerPage.Key.JOURNEY),
        "home": HomePage.load(),
        "principles": JourneyPrinciple.objects.filter(is_published=True),
        "stats": JourneyStat.objects.filter(is_published=True),
        "milestones": Milestone.objects.filter(is_published=True),
        "story_images": list(architecture[:2]),
        "featured_projects": Project.objects.for_homepage(HOME_LIST_COUNT),
    }
    return render(request, "pages/journey.html", context)


@require_GET
def media(request):
    images = list(MediaImage.objects.filter(is_published=True))
    used = {image.category for image in images}
    context = {
        "inner": inner_page(InnerPage.Key.MEDIA),
        "images": images,
        "categories": [(value, label) for value, label in MediaImage.Category.choices if value in used],
        "videos": [video for video in Video.objects.filter(is_published=True) if video.youtube_id],
        "press_items": PressItem.objects.filter(is_published=True).select_related("publication"),
        "press_publications": featured_publications(),
    }
    return render(request, "pages/media.html", context)


@require_GET
def contact(request):
    context = {
        "inner": inner_page(InnerPage.Key.CONTACT),
        "faqs": FAQ.objects.filter(is_published=True),
        "projects": Project.objects.published(),
    }
    return render(request, "pages/contact.html", context)


@require_GET
def page(request, slug):
    page = get_object_or_404(Page, slug=slug, is_published=True)
    return render(request, "pages/page.html", {"page": page})


@require_GET
def styleguide(request):
    colors = [
        {"name": "Ink", "value": "#0E0E0E", "class_name": "swatch--ink"},
        {"name": "Ivory", "value": "#F5F1EA", "class_name": "swatch--ivory"},
        {"name": "Stone", "value": "#D9D2C5", "class_name": "swatch--stone"},
        {"name": "Champagne", "value": "#B89B6A", "class_name": "swatch--champagne"},
        {"name": "Warm grey", "value": "#6E6A64", "class_name": "swatch--warm-grey"},
    ]
    return render(request, "pages/styleguide.html", {"colors": colors})


@require_GET
def robots_txt(request):
    lines = [
        "User-agent: *",
        "Disallow: /admin/",
        "Disallow: /api/",
        "Disallow: /styleguide",
        f"Sitemap: {request.build_absolute_uri(reverse('sitemap'))}",
    ]
    return HttpResponse("\n".join(lines) + "\n", content_type="text/plain")
