"""M3M Trump Tower Noida: logo, "The private lift", the private collection and the departures board.

New texts and images come from landing.seed(); new lists are filled once; the drive times get their kinds and
map links. The price band and the popup picture are no longer used, so their texts and images go.
"""

from django.db import migrations

SLUG = "m3m-trump-tower-noida"

NEW_LISTS = ["specs", "lift_floors", "vault"]


def forwards(apps, schema_editor):
    from projects import landing
    from projects.landing_pages import trump

    landing.seed(apps)
    landing.add_lists(apps, SLUG, NEW_LISTS)

    LandingItem = apps.get_model("projects", "LandingItem")
    LandingText = apps.get_model("projects", "LandingText")
    LandingImage = apps.get_model("projects", "LandingImage")
    items = LandingItem.objects.filter(page__slug=SLUG)
    for minutes, place, kind, query in trump.CONNECTIVITY:
        items.filter(list_key="connectivity", title=place, link="").update(subtitle=kind, link=query)
    LandingText.objects.filter(page__slug=SLUG, key__startswith="price_").delete()
    LandingImage.objects.filter(page__slug=SLUG, key__in=["price_bg", "popup_image"]).delete()


class Migration(migrations.Migration):
    dependencies = [("projects", "0023_cullinan_premium_sections")]

    operations = [migrations.RunPython(forwards, migrations.RunPython.noop)]
