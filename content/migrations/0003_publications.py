from django.db import migrations, models
import django.db.models.deletion

import core.images


def link_publications(apps, schema_editor):
    Publication = apps.get_model("content", "Publication")
    PressItem = apps.get_model("content", "PressItem")
    for item in PressItem.objects.all():
        publication, _ = Publication.objects.get_or_create(name=item.source.strip() or "Unknown")
        item.publication = publication
        item.save(update_fields=["publication"])


def unlink_publications(apps, schema_editor):
    PressItem = apps.get_model("content", "PressItem")
    for item in PressItem.objects.select_related("publication"):
        item.source = item.publication.name
        item.save(update_fields=["source"])


class Migration(migrations.Migration):
    dependencies = [
        ("content", "0002_menu_pages"),
    ]

    operations = [
        migrations.CreateModel(
            name="Publication",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=80, unique=True)),
                (
                    "logo",
                    core.images.ResizingImageField(
                        help_text="Official logo, ideally a wide PNG with a transparent or white background.",
                        upload_to="press/logos/",
                    ),
                ),
                ("website", models.URLField(blank=True)),
            ],
            options={"ordering": ["name"]},
        ),
        migrations.AddField(
            model_name="pressitem",
            name="publication",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.PROTECT, related_name="items", to="content.publication"
            ),
        ),
        migrations.RunPython(link_publications, unlink_publications),
        migrations.RemoveField(model_name="pressitem", name="source"),
        migrations.AlterField(
            model_name="pressitem",
            name="publication",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, related_name="items", to="content.publication"
            ),
        ),
        migrations.AlterField(
            model_name="pressitem",
            name="image",
            field=core.images.ResizingImageField(
                blank=True, help_text="Optional. Shown only if the publication has no logo.", upload_to="press/"
            ),
        ),
        migrations.AlterField(
            model_name="pressitem",
            name="title",
            field=models.CharField(help_text="The headline exactly as the publication printed it.", max_length=255),
        ),
        migrations.AlterField(
            model_name="pressitem",
            name="summary",
            field=models.TextField(help_text="One or two sentences on what the article reports."),
        ),
        migrations.AlterField(
            model_name="pressitem",
            name="article_url",
            field=models.URLField(help_text="Link to the article on the publication's website.", max_length=2000),
        ),
    ]
