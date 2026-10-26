from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_GET

from core.models import InnerPage, SiteSettings
from core.views import inner_page
from projects import billionaire_story, landing_content
from projects.models import BillionaireBlockPage, Project


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
    # A project with its own ad landing page (templates/projects/landing/<slug>.html) uses it.
    templates = [f"projects/landing/{project.slug}.html", "projects/detail.html"]
    return render(request, templates, {"project": project, "related": related, **landing_content.context_for(slug)})


@require_GET
def billionaire_block(request):
    # The story sections come from projects/billionaire_story.py; the hero, form and footer from the admin.
    page = BillionaireBlockPage.load()
    context = {
        **billionaire_story.context(),
        "page": page,
        "site": SiteSettings.load(),
        "residences": page.residences.filter(is_published=True),
        "home_url": reverse("core:home"),
    }
    return render(request, "projects/billionaire_block.html", context)
