from django.db import models


class Enquiry(models.Model):
    class Source(models.TextChoices):
        HERO = "hero", "Homepage hero form"
        POPUP = "popup", "Enquiry popup"
        GUIDED = "guided", "Project discovery (homepage)"
        CONTACT = "contact", "Contact page"
        BILLIONAIRE = "billionaire", "Billionaire Block page"
        BROCHURE = "brochure", "Billionaire Block brochure"
        LANDING = "landing", "Project landing page (ads)"
        PROJECTS = "projects", "Projects page form"
        JOURNEY = "journey", "Our Journey page form"
        MEDIA = "media", "Media page form"
        INSIGHTS = "insights", "Insights page form"
        CONTACT_BANNER = "contact_banner", "Contact page banner form"

    # The short forms on the menu-page banners: interest, name, mobile and email.
    BANNER_FORMS = {Source.PROJECTS, Source.JOURNEY, Source.MEDIA, Source.INSIGHTS, Source.CONTACT_BANNER}

    class CallTime(models.TextChoices):
        MORNING = "morning", "Morning · 9 AM–12 PM"
        AFTERNOON = "afternoon", "Afternoon · 12–3 PM"
        EVENING = "evening", "Evening · 3–6 PM"
        FLEXIBLE = "flexible", "Flexible"

    class Interest(models.TextChoices):
        RESIDENTIAL = "residential", "Residential"
        COMMERCIAL = "commercial", "Commercial"

    class Residency(models.TextChoices):
        INDIA = "india", "India"
        NRI = "nri", "Overseas (NRI)"

    class Status(models.TextChoices):
        NEW = "new", "New"
        CONTACTED = "contacted", "Contacted"
        QUALIFIED = "qualified", "Qualified"
        SITE_VISIT = "site_visit", "Site visit booked"
        CLOSED_WON = "won", "Closed – booked"
        CLOSED_LOST = "lost", "Closed – not interested"
        SPAM = "spam", "Spam / invalid"

    source = models.CharField(max_length=20, choices=Source.choices)
    project = models.ForeignKey(
        "projects.Project", null=True, blank=True, on_delete=models.SET_NULL, related_name="enquiries"
    )
    name = models.CharField(max_length=80, blank=True)
    phone = models.CharField(max_length=25, help_text="Stored in international format.")
    email = models.EmailField(max_length=254, blank=True)
    call_time = models.CharField(max_length=20, choices=CallTime.choices, blank=True)
    interest = models.CharField(max_length=20, choices=Interest.choices, blank=True)
    residency = models.CharField(max_length=20, choices=Residency.choices, blank=True)
    consent = models.BooleanField(default=False)
    message = models.TextField(blank=True, max_length=2000)

    page_url = models.URLField(max_length=1000, blank=True)
    utm_source = models.CharField(max_length=120, blank=True)
    utm_medium = models.CharField(max_length=120, blank=True)
    utm_campaign = models.CharField(max_length=120, blank=True)
    utm_term = models.CharField(max_length=120, blank=True)
    utm_content = models.CharField(max_length=120, blank=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.CharField(max_length=500, blank=True)

    status = models.CharField(max_length=20, choices=Status.choices, default=Status.NEW)
    assigned_to = models.ForeignKey(
        "auth.User", null=True, blank=True, on_delete=models.SET_NULL, related_name="assigned_enquiries"
    )
    notes = models.TextField(blank=True, help_text="Internal notes from the sales team.")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = "Enquiries"
        indexes = [models.Index(fields=["status", "-created_at"])]

    def __str__(self):
        return f"{self.name or self.email} · {self.get_source_display()}"
