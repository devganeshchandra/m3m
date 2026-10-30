"""Jacob & Co., The Cullinan and Trump Tower: their own call and WhatsApp numbers, the RERA block with its QR
code on the banner, and drive times that match Google Maps.

New texts and images come from landing.seed(). Routes now start from the project itself rather than the middle
of its sector, and each starting drive time is swapped for the one Google Maps shows; anything the content team
has edited stays as it is. The old RERA lines in the banners give way to the new block.
"""

from django.db import migrations

JACOB = "m3m-jacob-co-residences"
CULLINAN = "m3m-the-cullinan-residential"
TRUMP = "m3m-trump-tower-noida"

GOOGLE_NOTE = "Drive times as Google Maps shows them from the project for the fastest route; live traffic can change them."

TEXTS = {
    JACOB: [
        ("loc_origin", "Sector 97, Noida, Uttar Pradesh", "M3M Jacob & Co. Residences, Sector 97, Noida"),
        (
            "loc_note",
            "Approximate drive times in light traffic.",
            "Drive times as Google Maps shows them for the fastest route; live traffic can change them.",
        ),
    ],
    CULLINAN: [
        ("loc_origin", "Sector 94, Noida, Uttar Pradesh", "M3M The Cullinan, Sector 94, Noida"),
        ("loc_note", "*Travel times as stated by M3M India; they vary with route and traffic.", "*" + GOOGLE_NOTE),
    ],
    TRUMP: [
        ("loc_origin", "Sector 94, Noida, Uttar Pradesh", "Trump Towers Noida, Sector 94, Noida"),
        (
            "loc_note",
            "Travel times as stated by M3M India for its Sector 94 projects; they vary with route and traffic.",
            GOOGLE_NOTE,
        ),
        (
            "hero_legal",
            "UP RERA {rera} · Arrival court: artistic impression · Other images representative",
            "Arrival court: artistic impression · Other images representative",
        ),
    ],
}

# (page, list, place, old minutes, Google's minutes)
TIMES = [
    (JACOB, "drive_times", "Mall of Noida", "3", "4"),
    (JACOB, "drive_times", "Amity University", "8", "9"),
    (JACOB, "drive_times", "Botanical Garden Metro Station", "10", "12"),
    (JACOB, "drive_times", "Radisson Blu MBD Hotel", "16", "19"),
    (CULLINAN, "connectivity", "Amity University", "2", "7"),
    (CULLINAN, "connectivity", "Max Healthcare", "5", "31"),
    (CULLINAN, "connectivity", "Jasola Business Park", "5", "12"),
    (CULLINAN, "connectivity", "Apollo Hospital", "10", "17"),
    (CULLINAN, "connectivity", "Ansal Plaza", "12", "35"),
    (CULLINAN, "connectivity", "Radisson Blu, Sector 18", "12", "13"),
    (CULLINAN, "hero_stats", "to Amity University*", "2 min", "7 min"),
    (TRUMP, "connectivity", "Amity University", "2", "7"),
    (TRUMP, "connectivity", "Max Healthcare", "5", "32"),
    (TRUMP, "connectivity", "Jasola Business Park", "5", "12"),
    (TRUMP, "connectivity", "Apollo Hospital", "10", "16"),
    (TRUMP, "connectivity", "Ansal Plaza", "12", "36"),
    (TRUMP, "connectivity", "Radisson Blu, Sector 18", "12", "14"),
]


def forwards(apps, schema_editor):
    from projects import landing

    landing.seed(apps)
    for slug, changes in TEXTS.items():
        landing.replace_texts(apps, slug, changes)

    LandingItem = apps.get_model("projects", "LandingItem")
    LandingText = apps.get_model("projects", "LandingText")
    for slug, list_key, place, old, new in TIMES:
        LandingItem.objects.filter(page__slug=slug, list_key=list_key, title=place, value=old).update(value=new)
    LandingText.objects.filter(page__slug=JACOB, key="hero_rera").delete()
    LandingText.objects.filter(page__slug=CULLINAN, key="hero_caption_rera").delete()


class Migration(migrations.Migration):
    dependencies = [("projects", "0025_billionaire_premium_sections")]

    operations = [migrations.RunPython(forwards, migrations.RunPython.noop)]
