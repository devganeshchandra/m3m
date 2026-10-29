"""M3M The Cullinan: logo, "Cut your own Cullinan", route map, the private vault and a picture in the popup.

New texts and images come from landing.seed(); new lists are filled once; the drive times get their map
links and kinds. The old final form's texts and its "what you get" list are no longer used, so they go.
"""

from django.db import migrations

SLUG = "m3m-the-cullinan-residential"

NEW_LISTS = ["cert_cuts", "cert_slots", "vault"]


def forwards(apps, schema_editor):
    from projects import landing
    from projects.landing_pages import cullinan

    landing.seed(apps)
    landing.add_lists(apps, SLUG, NEW_LISTS)

    LandingItem = apps.get_model("projects", "LandingItem")
    LandingText = apps.get_model("projects", "LandingText")
    LandingImage = apps.get_model("projects", "LandingImage")
    items = LandingItem.objects.filter(page__slug=SLUG)
    for minutes, place, kind, query in cullinan.CONNECTIVITY:
        items.filter(list_key="connectivity", title=place, link="").update(subtitle=kind, link=query)
    items.filter(list_key="perks").delete()
    LandingText.objects.filter(page__slug=SLUG, key__in=["final_kicker", "final_title", "final_button"]).delete()
    LandingImage.objects.filter(page__slug=SLUG, key="final_image").delete()


class Migration(migrations.Migration):
    dependencies = [("projects", "0022_jacob_viewing_pass")]

    operations = [migrations.RunPython(forwards, migrations.RunPython.noop)]
