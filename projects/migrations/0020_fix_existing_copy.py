"""Correct copy that is already in the database (spelling review, October 2026).

Only the wrong words are replaced, so anything else the content team has edited stays as it is.
"""

from django.db import migrations, models

FIXES = [
    ("Website experience · Phase 1", ""),
    ("city's rhythm", "city’s rhythm"),
    ("residents' lounge", "residents’ lounge"),
    ("Residents' lounge", "Residents’ lounge"),
    ("it's free", "it’s free"),
    (" and choose “Overseas (NRI)” where asked.", "."),
    ("4,500 sq. ft.", "4,500 sq ft"),
    ("at Rs 1,839 crore", "at ₹1,839 crore"),
    (" A copy is also sent to you on WhatsApp.", ""),
    ("M3M Residences *by ELIE SAAB*", "Signature Residences *by ELIE SAAB*"),
    ("or request a call back.", "or request a callback."),
]

MODELS = [
    ("core", "SiteSettings"),
    ("core", "InnerPage"),
    ("core", "FAQ"),
    ("content", "PressItem"),
    ("projects", "Project"),
    ("projects", "BillionaireBlockPage"),
    ("projects", "LandingText"),
    ("projects", "LandingItem"),
]


def fix_copy(apps, schema_editor):
    for app_label, model_name in MODELS:
        model = apps.get_model(app_label, model_name)
        fields = [f.name for f in model._meta.fields if isinstance(f, (models.CharField, models.TextField))]
        for obj in model.objects.all():
            changed = []
            for field in fields:
                value = getattr(obj, field) or ""
                fixed = value
                for old, new in FIXES:
                    fixed = fixed.replace(old, new)
                if fixed != value:
                    setattr(obj, field, fixed)
                    changed.append(field)
            if changed:
                obj.save(update_fields=changed)


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0019_copy_fixes"),
        ("core", "0008_copy_fixes"),
        ("content", "0003_publications"),
    ]

    operations = [migrations.RunPython(fix_copy, migrations.RunPython.noop)]
