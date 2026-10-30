"""The website, page by page, and the admin screens that edit each part of it.

One map drives the admin home page (“Website map”), the admin sidebar and the “Edit this page” button that
staff see on the live site, so all three always agree on where each thing is edited.
"""

from django.urls import reverse


def _changelist(model_name, query=""):
    app = {
        "enquiry": "leads",
        "project": "projects", "landingpage": "projects", "landingitem": "projects", "billionaireblockpage": "projects",
        "homepage": "core", "innerpage": "core", "herobanner": "core", "page": "core", "faq": "core",
        "sitesettings": "core", "user": "auth", "group": "auth",
    }.get(model_name, "content")
    return reverse(f"admin:{app}_{model_name}_changelist") + (f"?{query}" if query else "")


def _change(obj):
    if obj is None:
        return ""
    opts = obj._meta
    return reverse(f"admin:{opts.app_label}_{opts.model_name}_change", args=[obj.pk])


def landing_page_url(slug):
    from projects.models import LandingPage

    return _change(LandingPage.objects.filter(slug=slug).first())


def inner_page_url(key):
    from core.models import InnerPage

    return _change(InnerPage.objects.filter(key=key).first())


def project_url(slug):
    from projects.models import Project

    return _change(Project.objects.filter(slug=slug).first())


def project_enquiries_url(slug):
    from projects.models import Project

    project = Project.objects.filter(slug=slug).first()
    return _changelist("enquiry", f"project__id__exact={project.pk}") if project else _changelist("enquiry")


def _edit(label, href, hint=""):
    return {"label": label, "href": href, "hint": hint}


WEBSITE_TEXTS = "website-texts"


def site_map():
    """Groups of pages: {title, intro, pages: [{name, url, note, edits: [{label, href, hint}]}]}."""
    from core.models import InnerPage
    from projects import landing
    from projects.models import Project

    texts = landing_page_url(WEBSITE_TEXTS)
    shared = _edit("Buttons & small headings", texts, "Website texts: the headings and buttons on this page")

    main = [
        {
            "name": "Homepage", "url": "/", "note": "The banner, every section heading and the projects shown.",
            "edits": [
                _edit("Homepage texts", _changelist("homepage"), "Banner words and each section’s heading and intro"),
                _edit("Banner pictures", _changelist("herobanner"), "The rotating pictures at the top"),
                _edit("Projects shown", _changelist("project", "is_featured__exact=1"), "Tick “Featured” on a project to show it"),
                _edit("Billionaire Block band", _changelist("billionaireblockpage"), "Homepage teaser section"),
                _edit("Journey figures", _changelist("journeystat"), "The numbers in “Our Journey”"),
                _edit("News on the homepage", _changelist("pressitem"), "Press stories"),
                shared,
            ],
        },
        {
            "name": "Projects", "url": "/projects", "note": "Every project, grouped by stage.",
            "edits": [
                _edit("Page banner & texts", inner_page_url(InnerPage.Key.PROJECTS)),
                _edit("Projects", _changelist("project"), "Add, remove or reorder projects; set each one’s stage"),
                shared,
            ],
        },
        {
            "name": "Our Journey", "url": "/our-journey", "note": "M3M’s story, values and milestones.",
            "edits": [
                _edit("Page banner & texts", inner_page_url(InnerPage.Key.JOURNEY)),
                _edit("Values", _changelist("journeyprinciple")),
                _edit("Figures", _changelist("journeystat")),
                _edit("Milestones", _changelist("milestone")),
                shared,
            ],
        },
        {
            "name": "Media Centre", "url": "/media-centre", "note": "Pictures, films and press coverage.",
            "edits": [
                _edit("Page banner & texts", inner_page_url(InnerPage.Key.MEDIA)),
                _edit("Pictures", _changelist("mediaimage")),
                _edit("Films", _changelist("video")),
                _edit("Press stories", _changelist("pressitem")),
                _edit("Publication logos", _changelist("publication")),
                shared,
            ],
        },
        {
            "name": "Insights", "url": "/insights", "note": "Articles and guides.",
            "edits": [
                _edit("Page banner & texts", inner_page_url(InnerPage.Key.INSIGHTS)),
                _edit("Articles", _changelist("insight"), "Write, edit or remove articles"),
                shared,
            ],
        },
        {
            "name": "Contact", "url": "/contact", "note": "Phone, address, map, form and questions.",
            "edits": [
                _edit("Page banner & texts", inner_page_url(InnerPage.Key.CONTACT)),
                _edit("Phone, email, address & map", _changelist("sitesettings")),
                _edit("Questions & answers", _changelist("faq")),
                shared,
            ],
        },
        {
            "name": "Legal pages", "url": "/disclaimer", "note": "Disclaimer, privacy policy and other text pages.",
            "edits": [_edit("Legal pages", _changelist("page"), "Add a page, then publish it to show it in the footer")],
        },
    ]

    def landing_entry(slug, name, note):
        return {
            "name": name, "url": f"/projects/{slug}", "note": note, "slug": slug,
            "edits": [
                _edit("All page content", landing_page_url(slug),
                      "Every text, picture and list, section by section, including its phone, WhatsApp and RERA block"),
                _edit("Project name, RERA no. & card", project_url(slug), "Also used on the Projects page"),
                _edit("Enquiries from this page", project_enquiries_url(slug)),
            ],
        }

    landing_pages = [
        landing_entry("m3m-jacob-co-residences", "M3M Jacob & Co. Residences", "Ad landing page · Sector 97, Noida"),
        landing_entry("m3m-the-cullinan-residential", "M3M The Cullinan", "Ad landing page · Sector 94, Noida"),
        landing_entry("m3m-trump-tower-noida", "M3M Trump Tower Noida", "Ad landing page · Sector 94, Noida"),
        {
            "name": "Billionaire Block", "url": "/billionaire-block", "note": "Sector 111, Gurugram · ELIE SAAB",
            "slug": "billionaire-block",
            "edits": [
                _edit("Banner, viewing form, brochure & RERA", _changelist("billionaireblockpage"),
                      "The top of the page, the private viewing form, residence choices and the footer"),
                _edit("All other page content", landing_page_url("billionaire-block"),
                      "Every other text, picture and list, section by section"),
                _edit("Enquiries from this page", _changelist("enquiry", "source__exact=billionaire")),
            ],
        },
    ]

    landing_slugs = set(landing.PAGES) | {WEBSITE_TEXTS}
    standard = [
        {
            "name": project.name, "url": project.get_absolute_url(), "note": "Standard project page",
            "edits": [
                _edit("Project page", _change(project), "Name, texts, highlights, floor plans and gallery"),
                _edit("Enquiries", project_enquiries_url(project.slug)),
            ],
        }
        for project in Project.objects.exclude(slug__in=landing_slugs).order_by("order", "name")
    ]

    everywhere = [
        {
            "name": "Header menu & shared texts", "url": "/", "note": "The menu, footer, enquiry popup and small headings on every page.",
            "edits": [
                _edit("Menu, footer & popup texts", texts, "Lists tab: the menu and Projects dropdown"),
            ],
        },
        {
            "name": "Phone, WhatsApp, address & footer", "url": "/contact", "note": "Used on every page except the ad landing pages, which have their own numbers.",
            "edits": [_edit("Contact & site settings", _changelist("sitesettings"))],
        },
    ]

    return [
        {"title": "Main website pages", "intro": "The pages in the website menu.", "pages": main},
        {"title": "Project landing pages", "intro": "The premium project pages used in advertising.", "pages": landing_pages},
        {"title": "Standard project pages", "intro": "Projects without their own landing page.", "pages": standard},
        {"title": "On every page", "intro": "Parts shared by the whole website.", "pages": everywhere},
    ]


def edits_for_path(path):
    """The admin screens that edit the page at `path`, for the “Edit this page” button on the site."""
    from content.models import Insight
    from core.models import Page

    path = "/" + path.strip("/") if path != "/" else "/"
    # An article or a legal page opens itself; every other page opens its entry in the map.
    if path.startswith("/insights/"):
        insight = Insight.objects.filter(slug=path.rsplit("/", 1)[-1]).first()
        if insight:
            return insight.title, [_edit("This article", _change(insight)), _edit("All articles", _changelist("insight"))]
    legal = Page.objects.filter(slug=path.lstrip("/")).first()
    if legal:
        return legal.title, [_edit("This page", _change(legal)), _edit("All legal pages", _changelist("page"))]
    for group in site_map():
        for page in group["pages"]:
            if page["url"] == path and group["title"] != "On every page":
                return page["name"], page["edits"]
    return None, []


def dashboard(request, context):
    """The admin home page: the website map, and the enquiries waiting for a call."""
    from leads.models import Enquiry

    waiting = Enquiry.objects.filter(status=Enquiry.Status.NEW)
    context.update(
        {
            "site_map": site_map(),
            "new_enquiries": waiting.count(),
            "new_enquiries_url": _changelist("enquiry", f"status__exact={Enquiry.Status.NEW}"),
            "all_enquiries_url": _changelist("enquiry"),
        }
    )
    return context
