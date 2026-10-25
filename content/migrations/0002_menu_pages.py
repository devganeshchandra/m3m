import django.utils.timezone
from django.db import migrations, models
from django.utils.text import slugify

import core.images


def fill_insight_slugs(apps, schema_editor):
    Insight = apps.get_model("content", "Insight")
    used = set()
    for insight in Insight.objects.order_by("pk"):
        base = slugify(insight.title)[:150] or f"insight-{insight.pk}"
        slug, n = base, 2
        while slug in used:
            slug, n = f"{base}-{n}", n + 1
        used.add(slug)
        insight.slug = slug
        if not insight.body:
            insight.body = insight.description
        insight.save(update_fields=["slug", "body"])


class Migration(migrations.Migration):
    dependencies = [
        ("content", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Milestone",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("order", models.PositiveIntegerField(default=0, help_text="Lower numbers appear first.")),
                ("is_published", models.BooleanField(default=True, verbose_name="Show on site")),
                ("marker", models.CharField(help_text="Short label on the timeline, e.g. “2010” or “Today”.", max_length=30)),
                ("title", models.CharField(max_length=140)),
                ("description", models.TextField(blank=True)),
                ("image", core.images.ResizingImageField(blank=True, upload_to="milestones/")),
            ],
            options={"verbose_name": "Journey milestone", "ordering": ["order", "id"], "abstract": False},
        ),
        migrations.CreateModel(
            name="Video",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("order", models.PositiveIntegerField(default=0, help_text="Lower numbers appear first.")),
                ("is_published", models.BooleanField(default=True, verbose_name="Show on site")),
                ("title", models.CharField(max_length=160)),
                ("youtube_url", models.URLField(help_text="Paste the YouTube link, e.g. https://www.youtube.com/watch?v=…")),
                ("description", models.CharField(blank=True, max_length=255)),
            ],
            options={"ordering": ["order", "id"], "abstract": False},
        ),
        migrations.AddField(
            model_name="mediaimage",
            name="category",
            field=models.CharField(
                choices=[
                    ("architecture", "Architecture"),
                    ("interiors", "Interiors"),
                    ("amenities", "Amenities"),
                    ("outdoors", "Outdoors & leisure"),
                ],
                default="architecture",
                max_length=20,
            ),
        ),
        migrations.RemoveField(model_name="insight", name="link_label"),
        migrations.RemoveField(model_name="insight", name="link_url"),
        migrations.AddField(
            model_name="insight",
            name="slug",
            field=models.SlugField(default="", max_length=160),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="insight",
            name="body",
            field=models.TextField(default=""),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="insight",
            name="author",
            field=models.CharField(default="M3M India Editorial", max_length=80),
        ),
        migrations.AddField(
            model_name="insight",
            name="published_on",
            field=models.DateField(default=django.utils.timezone.localdate),
        ),
        migrations.AddField(
            model_name="insight",
            name="is_featured",
            field=models.BooleanField(default=False, verbose_name="Feature at top of Insights page"),
        ),
        migrations.RunPython(fill_insight_slugs, migrations.RunPython.noop),
        migrations.AlterField(
            model_name="insight",
            name="slug",
            field=models.SlugField(help_text="Page address: /insights/<slug>", max_length=160, unique=True),
        ),
        migrations.AlterField(
            model_name="insight",
            name="body",
            field=models.TextField(
                help_text="The article. Leave a blank line between paragraphs. Start a line with ## to make it a sub-heading."
            ),
        ),
        migrations.AlterField(
            model_name="insight",
            name="description",
            field=models.TextField(help_text="Short summary shown on cards and in Google."),
        ),
        migrations.AlterModelOptions(
            name="insight",
            options={"ordering": ["order", "-published_on", "id"]},
        ),
    ]
