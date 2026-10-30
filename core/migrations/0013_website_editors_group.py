"""The “Website editors” group: everything the content team needs to run the website, without managing users.

Members can add, change and delete every page, project, landing page text, picture and list, article, press
story and setting, and can view, update and export enquiries (enquiries come only from the website, so they cannot
add them). Users and permissions stay with the superuser. Re-running keeps the group's permissions complete when
new content types are added.
"""

from django.contrib.auth.management import create_permissions
from django.db import migrations

CONTENT_APPS = ("core", "content", "projects")


def forwards(apps, schema_editor):
    # Permissions are normally created after migrations; make sure they exist now.
    for app_config in apps.get_app_configs():
        app_config.models_module = True
        create_permissions(app_config, apps=apps, verbosity=0)
        app_config.models_module = None

    Group = apps.get_model("auth", "Group")
    Permission = apps.get_model("auth", "Permission")
    group, _ = Group.objects.get_or_create(name="Website editors")
    # Only models that exist now: a database may still hold permissions of models removed long ago.
    current = [model._meta.model_name for model in apps.get_models() if model._meta.app_label in CONTENT_APPS]
    content = Permission.objects.filter(content_type__app_label__in=CONTENT_APPS, content_type__model__in=current)
    enquiries = Permission.objects.filter(
        content_type__app_label="leads", codename__in=["view_enquiry", "change_enquiry", "delete_enquiry"]
    )
    group.permissions.add(*content, *enquiries)


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0012_alter_homepage_projects_intro"),
        ("content", "0004_more_insights"),
        ("leads", "0007_banner_form_sources"),
        ("projects", "0029_website_texts"),
        ("auth", "0012_alter_user_first_name_max_length"),
        ("contenttypes", "0002_remove_content_type_name"),
    ]

    operations = [migrations.RunPython(forwards, migrations.RunPython.noop)]
