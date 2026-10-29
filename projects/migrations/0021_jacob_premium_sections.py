"""M3M Jacob & Co. Residences: logo, richer residences, floor plans, drive times and the private line.

New texts and images come from landing.seed(); new lists are filled once; texts that still have their
old starting wording get the new wording. Anything the content team has edited stays as it is.
"""

from django.db import migrations

SLUG = "m3m-jacob-co-residences"

TEXT_CHANGES = [
    ("res_eyebrow", "The residences", "The residences · 3, 4 & 5 BHK"),
    ("res_title", "An icon *in the making.*", "Where artistry *becomes an address.*"),
    (
        "res_lead",
        "Calm over chaos. Views over walls. Homes where your legacy resides.",
        "Three towers of branded 3, 4 and 5 BHK residences on Noida Expressway, where the artistry of Jacob & Co. "
        "meets the craftsmanship of M3M. Rooms flow into private balconies, light moves freely through every space, "
        "and the city becomes a view rather than a noise.",
    ),
    ("res_button", "Size & price", "Explore the floor plans"),
    ("loc_eyebrow", "Location", "Location advantage · Sector 97, Noida"),
    ("loc_title", "Sector 97, *Noida Expressway.*", "Everything, *minutes away.*"),
]

NEW_LISTS = ["res_photos", "res_pillars", "drive_times", "pl_choices", "pl_slots"]

NAV_ORDER = ["residences", "floor-plans", "commercial", "amenities", "gallery", "location"]


def forwards(apps, schema_editor):
    from projects import landing

    landing.seed(apps)
    landing.replace_texts(apps, SLUG, TEXT_CHANGES)
    landing.add_lists(apps, SLUG, NEW_LISTS)

    LandingItem = apps.get_model("projects", "LandingItem")
    nav = LandingItem.objects.filter(page__slug=SLUG, list_key="nav")
    if nav.exists() and not nav.filter(link="floor-plans").exists():
        LandingItem.objects.create(page=nav.first().page, list_key="nav", title="Floor plans", link="floor-plans")
        for item in nav:
            if item.link in NAV_ORDER:
                item.order = NAV_ORDER.index(item.link)
                item.save(update_fields=["order"])


class Migration(migrations.Migration):
    dependencies = [("projects", "0020_fix_existing_copy")]

    operations = [migrations.RunPython(forwards, migrations.RunPython.noop)]
