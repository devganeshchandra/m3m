"""Corrections from checking every page against M3M's official pages, UP RERA / HRERA and the launch coverage.

- The Line (retail and Pentsuites) is listed by M3M under ongoing projects, and Smartworld Sector 98 is registered and
  launched: none of them is a delivered landmark or an upcoming launch.
- The commercial project's official name is M3M Jewel Crest Avenue (high-street retail, fine dining and cafés).
- Smartworld Sector 98 offers 3 and 4 BHK residences (the 4,200+ sq ft four-bedroom homes are the Gurugram project).
- Jacob & Co.: the promoter is Mayfairsky Estates Pvt Ltd; no capital-appreciation or returns promises.
- The Cullinan: the 4Cs wording, the Avenue's "multi-level hub" and a labelled agent registration.
- Trump Tower: one size range does not cover both 4 and 5 BHK, so size is on request.
- Billionaire Block: registered with HRERA Gurugram (GGM/992/724/2025/95, 16.10.2025); the 250-acre township figure
  is unconfirmed; the featured quote follows Outlook Luxe word for word.

Only content still at its starting wording changes; anything the content team has edited stays as it is.
"""

from django.db import migrations

JACOB = "m3m-jacob-co-residences"
CULLINAN = "m3m-the-cullinan-residential"
TRUMP = "m3m-trump-tower-noida"
BILLIONAIRE = "billionaire-block"

STATUS = {
    "m3m-the-line-retail-shops": ("delivered", "current"),
    "m3m-the-line-pentsuites": ("delivered", "current"),
    "smartworld-noida-residential": ("upcoming", "current"),
    "smartworld-noida-commercial": ("upcoming", "current"),
}

# (project, field, old, new)
PROJECT_FIELDS = [
    ("m3m-jacob-jewel-crest-noida", "name", "M3M Jacob Jewel Crest Noida", "M3M Jewel Crest Avenue"),
    ("m3m-jacob-jewel-crest-noida", "offering", "Retail Shops, Food Court & Restaurant", "High-Street Retail, Fine Dining & Cafés"),
    (
        "m3m-jacob-jewel-crest-noida",
        "summary",
        "A retail, food court and restaurant destination at Sector 97, Noida Expressway.",
        "High-street retail, fine dining and cafés, integrated with the Jacob & Co. residences on Noida Expressway.",
    ),
    ("smartworld-noida-residential", "offering", "4 BHK Residence · 4,500 sq ft", "3 & 4 BHK Residences"),
    (
        "smartworld-noida-residential",
        "summary",
        "4 BHK residences, with a stated area of 4,500 sq ft, at Sector 98, Noida Expressway.",
        "3 and 4 BHK branded residences at Sector 98, Noida Expressway.",
    ),
    (
        "smartworld-noida-commercial",
        "offering",
        "1 & 2 BHK Serviced Apartments, Lockable Retail, Cafés & Restaurant",
        "1 & 2 BHK Serviced Suites, Retail, Cafés & Dining",
    ),
    (
        "smartworld-noida-commercial",
        "summary",
        "Serviced apartments, lockable retail, cafés and a restaurant at Sector 98, Noida Expressway.",
        "Serviced suites, retail, cafés and dining at Sector 98, Noida Expressway.",
    ),
]

TEXTS = {
    JACOB: [
        ("com_eyebrow", "Commercial · M3M Jacob Jewel Crest", "Commercial · M3M Jewel Crest Avenue"),
        (
            "com_lead",
            "Shops and F&B spaces within the Jacob & Co. project on Noida Expressway.",
            "High-street retail, fine dining and cafés, integrated with the residences.",
        ),
        ("loc_value_title", "Built for *capital appreciation.*", "Connected to *what matters.*"),
        (
            "loc_value_text",
            "Multi-modal transport & robust infrastructure for future capital appreciation.",
            "Noida Expressway, the metro and Central Noida, a short drive from home.",
        ),
    ],
    CULLINAN: [
        (
            "cert_lead",
            "A diamond is graded by its 4Cs. Grade your home in four taps: choose the carat, the cut and the moment "
            "we call, and your private certificate fills in as you go.",
            "Inspired by how a diamond is graded. Choose your residence, what we prepare and when we call, and your "
            "private certificate fills in as you go.",
        ),
        ("cert_step_4", "Certify · Where shall we reach you?", "Certificate · Where shall we reach you?"),
        ("rera_extra", "UPRERAAGT10202", "Agent RERA: UPRERAAGT10202"),
    ],
    BILLIONAIRE: [
        (
            "amenities_lead",
            "Seven worlds of resort living, every one reserved for residents. Hover or tap to open each.",
            "Seven worlds of resort living, planned for residents. Hover or tap to open each.",
        ),
        (
            "amenities_footnote",
            "Named in the ELIE SAAB project announcement. Final specifications follow the approved plans. Images are "
            "representative.",
            "As described in the ELIE SAAB project announcement. Final specifications follow the approved plans. Images "
            "are representative.",
        ),
        (
            "location_footnote",
            "From the project announcement. Travel times depend on the entrance, route and traffic.",
            "Indicative connectivity. Travel times depend on the entrance, route and traffic.",
        ),
        ("towers_pending", "Awaiting the sanctioned master plan", "To be confirmed in the sale documents"),
        (
            "sources_featured_quote",
            "ELIE SAAB’s first signature residences in India, at the heart of the Billionaire’s Block.",
            "The brand’s first branded residential developments in the country.",
        ),
    ],
}

# (page, list, title, field, old, new)
ITEMS = [
    (JACOB, "trust", "Developer", "text", "M3M India", "Mayfairsky Estates Pvt Ltd"),
    (JACOB, "pl_choices", "Investment outlook", "subtitle", "Growth, rentals and returns", "Pricing, plans and paperwork"),
    (JACOB, "pl_choices", "Investment outlook", "text", "an investment outlook", "the investment details"),
    (CULLINAN, "cert_cuts", "Investment outlook", "subtitle", "Growth, rentals and returns", "Pricing, plans and paperwork"),
    (TRUMP, "specs", "Size", "value", "4925 – 5685 sq.ft.", "On request"),
    (BILLIONAIRE, "community", "SCDA — integrated urban community", "subtitle", "250 acres · the township around it",
     "The township around it"),
    (BILLIONAIRE, "hotspots", "Waterfront views", "text", "Every residence is planned around views over the water.",
     "Residences planned with waterfront views."),
]


def forwards(apps, schema_editor):
    Project = apps.get_model("projects", "Project")
    LandingText = apps.get_model("projects", "LandingText")
    LandingItem = apps.get_model("projects", "LandingItem")
    LandingImage = apps.get_model("projects", "LandingImage")
    BillionaireBlockPage = apps.get_model("projects", "BillionaireBlockPage")
    HomePage = apps.get_model("core", "HomePage")

    for slug, (old, new) in STATUS.items():
        Project.objects.filter(slug=slug, status=old).update(status=new)
    for slug, field, old, new in PROJECT_FIELDS:
        Project.objects.filter(slug=slug, **{field: old}).update(**{field: new})

    for slug, changes in TEXTS.items():
        for key, old, new in changes:
            LandingText.objects.filter(page__slug=slug, key=key, value=old).update(value=new)

    for slug, list_key, title, field, old, new in ITEMS:
        LandingItem.objects.filter(page__slug=slug, list_key=list_key, title=title, **{field: old}).update(**{field: new})
    # Rename tags and labels last, once their other fields have been matched by the old title.
    LandingItem.objects.filter(page__slug=JACOB, list_key="trust", title="Developer").update(title="Promoter")
    for slug, list_key in ((JACOB, "pl_choices"), (CULLINAN, "cert_cuts")):
        LandingItem.objects.filter(page__slug=slug, list_key=list_key, title="Investment outlook").update(
            title="Investment details"
        )
    LandingItem.objects.filter(page__slug=CULLINAN, list_key="avenue_tags", title="Multi-level atrium").update(
        title="Multi-level hub"
    )
    LandingImage.objects.filter(
        page__slug=CULLINAN, key="avenue_b", alt="Multi-level atrium under a skylight, artistic impression"
    ).update(alt="A multi-level retail hub, artistic impression")

    # Billionaire Block: the township fact without the unconfirmed acreage, and the RERA registration on the timeline.
    LandingItem.objects.filter(page__slug=BILLIONAIRE, list_key="facts", title="Larger SCDA township", value="250").update(
        title="The township", value="SCDA", group="", text="Smart City Delhi Airport, M3M’s mixed-use master development"
    )
    milestones = LandingItem.objects.filter(page__slug=BILLIONAIRE, list_key="milestones")
    milestones.filter(subtitle="Approvals & RERA", group="next").update(
        title="October 2025", subtitle="RERA registered", text="Registered with HRERA Gurugram: GGM/992/724/2025/95.",
        group="done", order=0,
    )
    milestones.filter(title="January 2026", subtitle="Announcement").update(order=1)

    page = BillionaireBlockPage.objects.filter(pk=1).first()
    if page:
        if not page.rera_number:
            page.rera_number = "HRERA Gurugram GGM/992/724/2025/95 (16.10.2025)"
        page.about_facts = page.about_facts.replace(
            "250 acres | Smart City Delhi Airport township", "SCDA | Smart City Delhi Airport, M3M’s mixed-use township"
        )
        if page.security_text == "Smart City Delhi Airport: a mixed-use township of about 250 acres.":
            page.security_text = "Smart City Delhi Airport: M3M’s mixed-use township around the enclave."
        page.save()

    for home in HomePage.objects.filter(projects_intro__contains="Gurugram, Delhi NCR, Noida and Panipat"):
        home.projects_intro = home.projects_intro.replace(
            "Gurugram, Delhi NCR, Noida and Panipat", "Gurugram, Delhi, Noida and Panipat"
        )
        home.save(update_fields=["projects_intro"])


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0026_landing_contact_rera_drive_times"),
        ("core", "0011_banner_forms"),
    ]

    operations = [migrations.RunPython(forwards, migrations.RunPython.noop)]
