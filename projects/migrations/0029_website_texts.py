"""“Website texts” in the admin: the header menu, its Projects dropdown, and the headings, buttons and notes of
the header, footer, enquiry popup and menu pages that had no admin screen (projects/landing_pages/site.py)."""

from django.db import migrations


def forwards(apps, schema_editor):
    from projects import landing

    landing.seed(apps)


class Migration(migrations.Migration):
    dependencies = [("projects", "0028_alter_billionaireblockpage_about_facts_and_more")]

    operations = [migrations.RunPython(forwards, migrations.RunPython.noop)]
