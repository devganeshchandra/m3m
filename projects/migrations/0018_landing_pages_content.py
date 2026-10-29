from django.db import migrations


def seed_landing_pages(apps, schema_editor):
    from projects import landing

    landing.seed(apps)


class Migration(migrations.Migration):
    dependencies = [("projects", "0017_landing_pages")]

    operations = [migrations.RunPython(seed_landing_pages, migrations.RunPython.noop)]
