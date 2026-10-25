from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_GET

from content.models import JourneyStat
from core.models import InnerPage, SiteSettings
from core.views import inner_page
from projects.models import BillionaireBlockPage, BillionaireItem, Project


@require_GET
def project_list(request):
    page = inner_page(InnerPage.Key.PROJECTS)
    projects = list(Project.objects.published())
    texts = {
        Project.Status.DELIVERED: page.delivered_text,
        Project.Status.CURRENT: page.current_text,
        Project.Status.UPCOMING: page.upcoming_text,
    }
    collections = []
    # Shown in this order: what you can own now first, then what's next, then the track record.
    for index, status in enumerate((Project.Status.CURRENT, Project.Status.UPCOMING, Project.Status.DELIVERED), 1):
        name, subtitle = Project.COLLECTIONS[status]
        collections.append(
            {
                "key": status.value,
                "index": index,
                "name": name,
                "subtitle": subtitle,
                "text": texts[status],
                "projects": [p for p in projects if p.status == status],
            }
        )
    context = {
        "inner": page,
        "collections": collections,
        "total": len(projects),
        "residential_count": sum(p.is_residential for p in projects),
        "commercial_count": sum(p.is_commercial for p in projects),
        "locations": sorted({p.location for p in projects}),
    }
    return render(request, "projects/list.html", context)


@require_GET
def project_detail(request, slug):
    project = get_object_or_404(
        Project.objects.published().prefetch_related("highlights", "configurations", "gallery"), slug=slug
    )
    related = Project.objects.published().filter(status=project.status).exclude(pk=project.pk)[:3]
    return render(request, "projects/detail.html", {"project": project, "related": related})


@require_GET
def billionaire_block(request):
    page = BillionaireBlockPage.load()
    items = {value: [] for value in BillionaireItem.Section.values}
    for item in BillionaireItem.objects.filter(is_published=True):
        items[item.section].append(item)
    context = {
        "page": page,
        "site": SiteSettings.load(),
        "news": page.news.filter(is_published=True),
        "residences": page.residences.filter(is_published=True),
        "items": items,
        "amenity_groups": [
            (heading, items[section])
            for heading, section in [
                (page.amenities_indoor_heading, BillionaireItem.Section.AMENITY_INDOOR),
                (page.amenities_wellness_heading, BillionaireItem.Section.AMENITY_WELLNESS),
                (page.amenities_leisure_heading, BillionaireItem.Section.AMENITY_LEISURE),
            ]
            if items[section]
        ],
        "legacy_stats": JourneyStat.objects.filter(is_published=True),
        "delivered_projects": Project.objects.published().filter(status=Project.Status.DELIVERED),
        "home_url": reverse("core:home"),
    }
    return render(request, "projects/billionaire_block.html", context)
