"""Billionaire Block: hero figures, fact pictures, the couture residence, community circles, destination
pictures, the timeline, the featured source and the private viewing invitation.

New texts and images come from landing.seed(); new lists are filled once. Existing items only gain the new
fields where they are still empty, and a text or picture is swapped only while it is the starting one.
The slideshow is replaced by the pictures on the four facts, and the scroll hint by the hero's figures, so
they go.
"""

from django.db import migrations

SLUG = "billionaire-block"

NEW_LISTS = ["hero_stats", "hotspots", "milestones", "visit_modes", "visit_purposes", "visit_slots"]

TEXT_CHANGES = [
    ("details_eyebrow", "Announced details", "The couture residence"),
    ("details_title", "A clearly defined *luxury* residence.", "A residence *tailored* like haute couture."),
]


def forwards(apps, schema_editor):
    from projects import landing
    from projects.landing_pages import billionaire

    landing.seed(apps)
    landing.add_lists(apps, SLUG, NEW_LISTS)
    landing.replace_texts(apps, SLUG, TEXT_CHANGES)

    LandingItem = apps.get_model("projects", "LandingItem")
    LandingImage = apps.get_model("projects", "LandingImage")
    items = LandingItem.objects.filter(page__slug=SLUG)

    items.filter(list_key="plan_slides").delete()
    # The hero's figures take the place of the scroll hint.
    apps.get_model("projects", "LandingText").objects.filter(page__slug=SLUG, key__startswith="hero_scroll").delete()

    for title, _value, _group, _text, image, alt in billionaire.FACTS:
        items.filter(list_key="facts", title=title, image="").update(
            image=landing._copy_static(billionaire, image), image_alt=alt
        )

    for card in billionaire.ITEMS["community"]:
        items.filter(list_key="community", value=card["value"], subtitle="").update(subtitle=card["subtitle"])

    for title, kind, line, query, image, alt in billionaire.ROUTES:
        route = items.filter(list_key="routes", title=title)
        route.filter(subtitle="").update(subtitle=kind)
        route.filter(text="").update(text=line)
        route.filter(link="").update(link=query)
        route.filter(image="").update(image=landing._copy_static(billionaire, image), image_alt=alt)

    items.filter(list_key="sources", link__startswith="https://luxe.outlookindia.com/", group="").update(group="featured")

    # The living room moves to the couture residence; the ELIE SAAB section opens on the salon.
    main = billionaire.IMAGES[0]
    LandingImage.objects.filter(
        page__slug=SLUG, key="brand_main", image="landing/billionaire-block/living-room.jpg"
    ).update(image=landing._copy_static(billionaire, main[3]), alt=main[4])


class Migration(migrations.Migration):
    dependencies = [("projects", "0024_trump_premium_sections")]

    operations = [migrations.RunPython(forwards, migrations.RunPython.noop)]
