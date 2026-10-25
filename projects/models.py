from django.db import models
from django.urls import reverse

from core.images import ResizingImageField
from core.models import SingletonModel


class ProjectQuerySet(models.QuerySet):
    def published(self):
        return self.filter(is_published=True)

    def for_homepage(self, limit=3):
        """Featured projects first; topped up from the rest when fewer are featured."""
        projects = list(self.published().filter(is_featured=True)[:limit])
        if len(projects) < limit:
            exclude = [p.pk for p in projects]
            projects += list(self.published().exclude(pk__in=exclude)[: limit - len(projects)])
        return projects


class Project(models.Model):
    """A project and its landing page at /projects/<slug>."""

    class Status(models.TextChoices):
        DELIVERED = "delivered", "Delivered Landmarks (completed & handed over)"
        CURRENT = "current", "Now Presenting (available now)"
        UPCOMING = "upcoming", "On the Horizon (upcoming)"

    # Public names and descriptions of each collection on the Projects page.
    COLLECTIONS = {
        Status.DELIVERED: ("Delivered Landmarks", "Completed & handed over"),
        Status.CURRENT: ("Now Presenting", "Available to own today"),
        Status.UPCOMING: ("On the Horizon", "Upcoming launches"),
    }

    name = models.CharField(max_length=120)
    slug = models.SlugField(
        unique=True,
        max_length=120,
        help_text="Used in the page address: /projects/your-project-name. Changing it breaks old links.",
    )
    category = models.CharField(
        max_length=80, help_text="Brand / collection shown above the name, e.g. “M3M The Line”."
    )
    is_residential = models.BooleanField("Residential", default=False)
    is_commercial = models.BooleanField("Commercial", default=False)
    offering = models.CharField(max_length=160, help_text="e.g. “3, 4 & 5 BHK Apartments”.")
    location = models.CharField(max_length=120, help_text="e.g. “Sector 97, Noida Expressway”.")
    city = models.CharField(max_length=60, default="Noida")
    rera = models.CharField("RERA number", max_length=80)
    image = ResizingImageField(upload_to="projects/", help_text="Main project image (landscape).")
    summary = models.TextField(help_text="Short description used on the card, page and in Google.")
    status = models.CharField(
        "Collection",
        max_length=20,
        choices=Status.choices,
        default=Status.CURRENT,
        help_text="Which collection the project appears in on the Projects page.",
    )
    timeline_note = models.CharField(
        max_length=80,
        blank=True,
        help_text="Optional short note on the card, e.g. “Possession from 2029” or “Handed over 2024”.",
    )
    is_featured = models.BooleanField(
        "Show on homepage",
        default=False,
        help_text="The homepage shows up to 3 featured projects (in order).",
    )

    # Landing page
    headline = models.CharField(
        max_length=120, default="A place to make your own.", help_text="Big heading in the overview."
    )
    overview_label = models.CharField(max_length=60, default="The address")
    description = models.TextField(
        blank=True, help_text="Optional longer description. Leave a blank line between paragraphs."
    )
    brochure = models.FileField(upload_to="brochures/", blank=True, help_text="Optional PDF brochure.")
    map_embed_url = models.URLField(
        blank=True,
        max_length=1000,
        help_text="Optional Google Maps “Embed a map” link (the src=… URL only).",
    )

    # SEO
    seo_title = models.CharField(max_length=120, blank=True, help_text="Defaults to the project name.")
    seo_description = models.CharField(max_length=300, blank=True, help_text="Defaults to the summary.")

    order = models.PositiveIntegerField(default=0, help_text="Lower numbers appear first.")
    is_published = models.BooleanField("Show on site", default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ProjectQuerySet.as_manager()

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("projects:detail", args=[self.slug])

    @property
    def collection_name(self):
        return self.COLLECTIONS[self.status][0]

    @property
    def interests(self):
        return [
            interest
            for interest, enabled in (("residential", self.is_residential), ("commercial", self.is_commercial))
            if enabled
        ]


class ProjectHighlight(models.Model):
    project = models.ForeignKey(Project, related_name="highlights", on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    text = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return self.title


class ProjectConfiguration(models.Model):
    """A unit type / floor plan row, e.g. “3 BHK · 2,450 sq. ft.”."""

    project = models.ForeignKey(Project, related_name="configurations", on_delete=models.CASCADE)
    unit_type = models.CharField(max_length=80)
    size = models.CharField(max_length=80, blank=True)
    price = models.CharField(max_length=80, blank=True, help_text="e.g. “Price on request”.")
    floor_plan = ResizingImageField(upload_to="floor-plans/", blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "Configuration / floor plan"
        verbose_name_plural = "Configurations / floor plans"

    def __str__(self):
        return self.unit_type


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name="gallery", on_delete=models.CASCADE)
    image = ResizingImageField(upload_to="projects/gallery/")
    caption = models.CharField(max_length=160, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "Gallery image"

    def __str__(self):
        return self.caption or f"Image {self.pk}"


class BillionaireBlockPage(SingletonModel):
    """Headings, texts and media of the Billionaire Block page at /billionaire-block.

    Lists (figures, features, club, services, security, distances, gallery, specifications) are
    “Billionaire Block content items”; residence types are edited in the tab above.
    """

    # Hero
    hero_video = models.FileField(
        upload_to="billionaire-block/", blank=True, help_text="Silent MP4 loop, 10–20 seconds. Leave empty to show the image."
    )
    hero_image = ResizingImageField(
        upload_to="billionaire-block/", blank=True, help_text="Shown while the video loads, and on its own without a video."
    )
    hero_image_alt = models.CharField(max_length=160, default="Billionaire Block towers above the clouds, artistic impression")
    eyebrow = models.CharField(max_length=80, default="By invitation only")
    title = models.CharField(max_length=60, default="Billionaire Block")
    tagline = models.CharField(max_length=160, default="Residences beyond reach. Reserved for the few.")

    # Teaser shown on the homepage, linking to this page
    teaser_label = models.CharField(max_length=80, default="The future of M3M")
    teaser_heading = models.CharField(max_length=160, default="Something extraordinary is rising.")
    teaser_text = models.TextField(
        default=(
            "A 170-acre enclave of globally branded residences in Sector 111, Gurugram, beginning with Signature "
            "Residences by ELIE SAAB. Conceived for the very few, and opening by private invitation."
        )
    )
    teaser_button = models.CharField(max_length=60, default="Explore Billionaire Block")

    # About the project and what is being built (just below the hero)
    about_label = models.CharField(max_length=80, default="About the project")
    about_heading = models.CharField(max_length=160, default="A 170-acre address for the world’s finest names.")
    about_text = models.TextField(
        default=(
            "The Billionaire’s Block is a 170-acre enclave within M3M’s Smart City Delhi Airport township, in "
            "Sector 111 on Gurugram’s Dwarka Expressway. It is planned as a carefully curated district, designed to "
            "host a select group of globally renowned branded residences.\n\n"
            "Rather than a single tower, it is conceived as one integrated destination, where architecture, "
            "landscape, wellness, hospitality and resident services are planned together from the first line of the "
            "master plan."
        ),
        help_text="Leave a blank line between paragraphs.",
    )
    about_image = ResizingImageField(upload_to="billionaire-block/", blank=True)
    about_image_2 = ResizingImageField(
        upload_to="billionaire-block/", blank=True, help_text="Optional. Stacked under the first image."
    )
    about_facts = models.TextField(
        blank=True,
        default=(
            "170 acres | The Billionaire’s Block enclave\n"
            "Sector 111 | Dwarka Expressway, Gurugram\n"
            "2026 | India Property Awards: Master Development"
        ),
        help_text="One per line, as “figure | label”.",
    )
    building_label = models.CharField(max_length=80, default="What we are building")
    building_heading = models.CharField(max_length=160, default="Branded residences, couture-coded.")
    building_text = models.TextField(
        default=(
            "The first address in the enclave is Signature Residences by ELIE SAAB: 300 four-bedroom homes of "
            "4,200 to 4,650 sq ft, with generous floor-to-ceiling heights, waterfront views and outdoor living areas "
            "with private jacuzzis.\n\n"
            "The interiors are a creative collaboration with designer Carlo Colombo, furnished from the ELIE SAAB "
            "Maison collection and crafted in Italy. Concierge services, a spa, swimming pools, fitness centres and "
            "residents’ lounges complete the everyday."
        ),
        help_text="Leave a blank line between paragraphs.",
    )
    building_image = ResizingImageField(upload_to="billionaire-block/", blank=True)
    building_image_2 = ResizingImageField(
        upload_to="billionaire-block/", blank=True, help_text="Optional. Stacked under the first image."
    )
    building_points = models.TextField(
        blank=True,
        default=(
            "300 four-bedroom residences\n"
            "4,200 to 4,650 sq ft each\n"
            "Interiors with Carlo Colombo\n"
            "Completion scheduled for 2030"
        ),
        help_text="One point per line.",
    )
    building_note = models.CharField(
        max_length=200, blank=True, default="Figures as reported by Business Today and Outlook Luxe, January 2026."
    )

    # News (the stories themselves are in the “News” tab)
    news_label = models.CharField(max_length=80, default="In the news")
    news_heading = models.CharField(max_length=160, default="The plan, as reported.")
    news_intro = models.TextField(
        default="What leading publications have reported about the Billionaire’s Block and its first branded residences."
    )

    # Manifesto
    manifesto_heading = models.CharField(max_length=160, default="Some addresses are bought. This one is earned.")
    manifesto_text = models.TextField(
        default=(
            "A private vertical estate for the families who shape the country’s industry, capital and culture. "
            "Few residences. Rare materials. A culture of service that never needs to be asked."
        )
    )

    # Architecture
    architecture_label = models.CharField(max_length=80, default="Architecture & design")
    architecture_heading = models.CharField(max_length=160, default="Sculpted by light. Composed for permanence.")
    architecture_text = models.TextField(
        default=(
            "Ribbons of ivory stone wrap each tower like silk, opening and closing to frame the sky. Every façade "
            "is turned to the light, so no two hours look the same.\n\n"
            "Inside, the plan is drawn around how a family actually lives: a formal wing for receiving, a private "
            "wing for rest, and a discreet service spine that keeps the household running unseen."
        ),
        help_text="Leave a blank line between paragraphs.",
    )
    architecture_image = ResizingImageField(upload_to="billionaire-block/", blank=True)
    credit_1_label = models.CharField(max_length=40, blank=True, default="Architecture")
    credit_1_value = models.CharField(max_length=120, blank=True, default="International design studio, revealed at the private preview")
    credit_2_label = models.CharField(max_length=40, blank=True, default="Interiors")
    credit_2_value = models.CharField(max_length=120, blank=True, default="Bespoke interiors atelier")
    credit_3_label = models.CharField(max_length=40, blank=True, default="Landscape")
    credit_3_value = models.CharField(max_length=120, blank=True, default="Sky gardens by a landscape atelier")

    # Section headings
    residences_label = models.CharField(max_length=80, default="The residences")
    residences_heading = models.CharField(max_length=160, default="Three ways to live above it all.")
    features_label = models.CharField(max_length=80, default="Residence features")
    features_heading = models.CharField(max_length=160, default="Details that are never compromised.")
    features_intro = models.TextField(
        default="Nine details define every residence. Each is specified once, and never value-engineered away."
    )
    club_label = models.CharField(max_length=80, default="The club")
    club_heading = models.CharField(max_length=160, default="A private club, reserved for residents.")
    club_intro = models.TextField(
        default="Eleven spaces for wellness, leisure and the art of hosting. Open only to residents and their guests."
    )
    amenities_label = models.CharField(max_length=80, default="The amenities")
    amenities_heading = models.CharField(max_length=160, default="A world of amenities, beyond the club.")
    amenities_intro = models.TextField(
        default="Indoor play, outdoor wellness and gardens for every generation, all within the enclave."
    )
    amenities_indoor_heading = models.CharField(max_length=120, default="World-class indoor amenities")
    amenities_wellness_heading = models.CharField(max_length=120, default="Amenities curated for wellness")
    amenities_leisure_heading = models.CharField(max_length=120, default="Leisure spaces for all generations")
    services_label = models.CharField(max_length=80, default="Lifestyle services")
    services_heading = models.CharField(max_length=160, default="Hotel-grade service. At home.")
    services_intro = models.TextField(
        default="A dedicated residence team, on call at every hour, so the household runs as smoothly as your business."
    )
    security_label = models.CharField(max_length=80, default="Privacy & security")
    security_heading = models.CharField(max_length=160, default="Privacy is the rarest luxury.")
    security_text = models.TextField(
        default="Discretion is designed in, not added on. You choose who arrives, how, and when.",
    )
    security_image = ResizingImageField(upload_to="billionaire-block/", blank=True)
    location_label = models.CharField(max_length=80, default="Location")
    location_heading = models.CharField(max_length=160, default="At the centre of everything that matters.")
    location_text = models.TextField(
        default="Moments from Gurugram’s business districts, its finest schools and hospitals, and the city’s golf greens."
    )
    location_note = models.CharField(max_length=160, default="Indicative travel times by car, outside peak hours.")
    map_embed_url = models.URLField(
        max_length=1000,
        default="https://www.google.com/maps?q=Golf+Course+Road,+Gurugram&output=embed",
        help_text="Google Maps → Share → Embed a map → copy the src=… link.",
    )
    gallery_label = models.CharField(max_length=80, default="Gallery")
    gallery_heading = models.CharField(max_length=160, default="A closer look.")
    specs_label = models.CharField(max_length=80, default="Specifications")
    specs_heading = models.CharField(max_length=160, default="Specified without compromise.")
    specs_intro = models.TextField(
        default="Materials and systems chosen for how they feel on the first day, and how they will age over decades."
    )
    specs_image = ResizingImageField(upload_to="billionaire-block/", blank=True)

    # Developer legacy (figures come from “Journey statistics”, projects from “Delivered Landmarks”)
    legacy_label = models.CharField(max_length=80, default="The developer")
    legacy_heading = models.CharField(max_length=160, default="A legacy written in landmarks.")
    legacy_text = models.TextField(
        default=(
            "Since 2010, M3M India has built a reputation on addresses that change how a city sees itself. "
            "Billionaire Block is the most personal expression of that journey: fewer homes, made with more care "
            "than ever before."
        )
    )

    # Private viewing form
    form_label = models.CharField(max_length=80, default="Private viewing")
    form_heading = models.CharField(max_length=120, default="Request a Private Viewing")
    form_intro = models.TextField(
        default="A senior relationship director will arrange a private presentation at a time and place of your choosing."
    )
    form_success_title = models.CharField(max_length=120, default="Your request is received.")
    form_success_text = models.TextField(
        default="A senior relationship director will call you personally within one working day to confirm your private viewing."
    )
    form_note = models.CharField(max_length=160, default="Your details are held in strict confidence.")
    viewing_steps = models.TextField(
        blank=True,
        default=(
            "A personal call from a senior relationship director\n"
            "A private presentation at a time and place you choose\n"
            "A chauffeured visit to the Billionaire’s Block"
        ),
        help_text="“What happens next”, one step per line.",
    )

    # Brochure
    brochure = models.FileField(upload_to="billionaire-block/", blank=True, help_text="PDF. Visitors share their name and phone first.")
    brochure_heading = models.CharField(max_length=120, default="The private brochure")
    brochure_text = models.CharField(
        max_length=200, default="Share your name and number and the brochure is yours. A copy is also sent to you on WhatsApp."
    )

    # Footer
    rera_number = models.CharField(max_length=80, default="To be updated", help_text="Project RERA registration number.")
    footer_disclaimer = models.TextField(
        default=(
            "All images are artistic impressions. Figures, specifications, amenities and services are indicative and "
            "subject to approvals and the final project documents. This page is not an offer or an invitation to buy."
        )
    )

    seo_title = models.CharField(max_length=120, default="Billionaire Block by M3M | Residences by invitation only")
    seo_description = models.CharField(
        max_length=300,
        default=(
            "Billionaire Block by M3M: a strictly limited collection of ultra-luxury residences with a private club "
            "and hotel-grade service. Request a private viewing."
        ),
    )

    class Meta:
        verbose_name = "Billionaire Block page"
        verbose_name_plural = "Billionaire Block page"

    def __str__(self):
        return "Billionaire Block page"

    def get_absolute_url(self):
        return reverse("projects:billionaire_block")

    @staticmethod
    def _lines(text):
        return [line.strip() for line in text.splitlines() if line.strip()]

    @property
    def about_fact_list(self):
        facts = []
        for line in self._lines(self.about_facts):
            value, _, label = line.partition("|")
            facts.append((value.strip(), label.strip()))
        return facts

    @property
    def building_point_list(self):
        return self._lines(self.building_points)

    @property
    def viewing_step_list(self):
        return self._lines(self.viewing_steps)

    @property
    def credits(self):
        pairs = [
            (self.credit_1_label, self.credit_1_value),
            (self.credit_2_label, self.credit_2_value),
            (self.credit_3_label, self.credit_3_value),
        ]
        return [(label, value) for label, value in pairs if label and value]


class BillionaireResidence(models.Model):
    """A residence type, e.g. Sky Villas, with its floor plan."""

    page = models.ForeignKey(BillionaireBlockPage, related_name="residences", on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    tagline = models.CharField(max_length=160, blank=True)
    image = ResizingImageField(upload_to="billionaire-block/")
    image_alt = models.CharField(max_length=160, blank=True)
    size = models.CharField(max_length=80, help_text="e.g. “10,000 – 12,500 sq ft”.")
    configuration = models.CharField(max_length=120, help_text="e.g. “4 & 5 bedrooms with staff quarters”.")
    features = models.TextField(blank=True, help_text="One feature per line.")
    floor_plan = ResizingImageField(
        upload_to="billionaire-block/floor-plans/", blank=True, help_text="Leave empty to offer the plan on request."
    )
    order = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField("Show on site", default=True)

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "Residence type"

    def __str__(self):
        return self.name

    @property
    def feature_list(self):
        return [line.strip() for line in self.features.splitlines() if line.strip()]


class BillionaireItem(models.Model):
    """One entry in a list on the Billionaire Block page; `section` decides where it appears."""

    class Section(models.TextChoices):
        STAT = "stat", "Key numbers"
        FEATURE = "feature", "Residence features"
        CLUB = "club", "The club (with image)"
        SERVICE = "service", "Lifestyle services"
        SECURITY = "security", "Privacy & security"
        LOCATION = "location", "Location distances"
        GALLERY = "gallery", "Gallery (with image)"
        AMENITY_INDOOR = "amenity_indoor", "Amenities: indoor"
        AMENITY_WELLNESS = "amenity_wellness", "Amenities: wellness"
        AMENITY_LEISURE = "amenity_leisure", "Amenities: leisure"
        SPEC = "spec", "Specifications"

    section = models.CharField(max_length=20, choices=Section.choices)
    title = models.CharField(max_length=120, help_text="Name, label or caption.")
    value = models.CharField(
        max_length=60, blank=True, help_text="Key numbers: the figure, e.g. “12,000+”. Distances: the time, e.g. “15 min”."
    )
    text = models.TextField(blank=True, help_text="Short description. Key numbers: the unit, e.g. “sq ft”.")
    image = ResizingImageField(upload_to="billionaire-block/", blank=True)
    image_alt = models.CharField(max_length=160, blank=True)
    order = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField("Show on site", default=True)

    class Meta:
        ordering = ["section", "order", "id"]
        verbose_name = "Billionaire Block content item"

    def __str__(self):
        return f"{self.get_section_display()}: {self.title}"


class BillionaireNews(models.Model):
    """A published story about the project, shown as a card that opens in a popup."""

    page = models.ForeignKey(BillionaireBlockPage, related_name="news", on_delete=models.CASCADE)
    tag = models.CharField(max_length=40, blank=True, help_text="One word, e.g. “Launch” or “Pricing”.")
    title = models.CharField(max_length=160)
    publication = models.CharField(max_length=80, help_text="e.g. “Business Today” or “PTI via The Week”.")
    published_on = models.DateField()
    summary = models.CharField(max_length=240, help_text="Shown on the card.")
    body = models.TextField(help_text="Shown in the popup. Leave a blank line between paragraphs.")
    key_points = models.TextField(blank=True, help_text="Shown in the popup. One point per line.")
    url = models.URLField("Link to the article", max_length=500)
    is_press_release = models.BooleanField(
        "Paid press release", default=False, help_text="Adds a note that the source is a sponsored release."
    )
    order = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField("Show on site", default=True)

    class Meta:
        ordering = ["order", "-published_on", "id"]
        verbose_name = "News story"
        verbose_name_plural = "News"

    def __str__(self):
        return self.title

    @property
    def key_point_list(self):
        return [line.strip() for line in self.key_points.splitlines() if line.strip()]
