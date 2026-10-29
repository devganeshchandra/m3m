"""M3M Jacob & Co. Residences: the final section becomes a private site visit pass; the private line drops days.

New texts come from landing.seed(). Texts and list items that still have their old starting wording get the new
wording; anything the content team has edited stays as it is.
"""

from django.db import migrations

SLUG = "m3m-jacob-co-residences"

TEXT_CHANGES = [
    ("final_eyebrow", "Private preview", "By invitation · Private site visit"),
    ("final_title", "Own an icon *in the making.*", "See it before *the world does.*"),
    ("final_button", "Request a callback", "Reserve my viewing"),
]

PERK_CHANGES = [
    ("Brochure & launch price list", "Chauffeur pickup from your home or office"),
    ("Floor plans for 3, 4 & 5 BHK", "A private walkthrough with your relationship manager"),
    ("Site visit at a time that suits you", "The launch price list and floor plans, in hand"),
]

SLOT_LETTERS = {
    "morning": "in the morning",
    "afternoon": "in the afternoon",
    "evening": "in the evening",
    "flexible": "whenever suits you",
}


def forwards(apps, schema_editor):
    from projects import landing

    landing.seed(apps)
    landing.replace_texts(apps, SLUG, TEXT_CHANGES)

    LandingItem = apps.get_model("projects", "LandingItem")
    items = LandingItem.objects.filter(page__slug=SLUG)
    for old, new in PERK_CHANGES:
        items.filter(list_key="perks", title=old).update(title=new)
    for value, letter in SLOT_LETTERS.items():
        items.filter(list_key="pl_slots", value=value, text="").update(text=letter)
    # The private line now asks only for a time of day.
    items.filter(list_key="pl_days").delete()


class Migration(migrations.Migration):
    dependencies = [("projects", "0021_jacob_premium_sections")]

    operations = [migrations.RunPython(forwards, migrations.RunPython.noop)]
