from django.contrib import admin
from django.utils.html import format_html
from unfold.admin import ModelAdmin, StackedInline, TabularInline

from core.admin import SingletonAdmin
from projects.models import (
    BillionaireBlockPage,
    BillionaireItem,
    BillionaireNews,
    BillionaireResidence,
    Project,
    ProjectConfiguration,
    ProjectHighlight,
    ProjectImage,
)


class ProjectHighlightInline(TabularInline):
    model = ProjectHighlight
    extra = 0
    tab = True


class ProjectConfigurationInline(TabularInline):
    model = ProjectConfiguration
    extra = 0
    tab = True


class ProjectImageInline(StackedInline):
    model = ProjectImage
    extra = 0
    tab = True


@admin.register(Project)
class ProjectAdmin(ModelAdmin):
    list_display = ["thumbnail", "name", "status", "is_featured", "location", "order", "is_published", "enquiry_count"]
    list_display_links = ["thumbnail", "name"]
    list_editable = ["status", "is_featured", "order", "is_published"]
    list_filter = ["status", "is_published", "is_featured", "category", "is_residential", "is_commercial"]
    search_fields = ["name", "category", "location", "rera"]
    prepopulated_fields = {"slug": ["name"]}
    inlines = [ProjectHighlightInline, ProjectConfigurationInline, ProjectImageInline]
    fieldsets = [
        (
            "Project card",
            {
                "fields": [
                    ("name", "slug"),
                    "category",
                    ("is_residential", "is_commercial"),
                    "offering",
                    ("location", "city"),
                    "rera",
                    "image",
                    "summary",
                    ("status", "timeline_note"),
                    ("is_featured", "order", "is_published"),
                ]
            },
        ),
        (
            "Landing page",
            {
                "fields": ["overview_label", "headline", "description", "brochure", "map_embed_url"],
                "description": "Highlights, floor plans and the gallery are in the tabs above.",
            },
        ),
        ("Search engines", {"fields": ["seo_title", "seo_description"], "classes": ["collapse"]}),
    ]

    @admin.display(description="")
    def thumbnail(self, obj):
        if not obj.image:
            return ""
        return format_html('<img src="{}" style="width:72px;height:48px;object-fit:cover;border-radius:4px">', obj.image.url)

    @admin.display(description="Enquiries")
    def enquiry_count(self, obj):
        return obj.enquiries.count()


class BillionaireResidenceInline(StackedInline):
    model = BillionaireResidence
    extra = 0
    tab = True
    fields = [("name", "order", "is_published"), "tagline", ("size", "configuration"), "features", ("image", "image_alt"), "floor_plan"]


class BillionaireNewsInline(StackedInline):
    model = BillionaireNews
    extra = 0
    tab = True
    fields = [
        ("title", "tag"),
        ("publication", "published_on"),
        "summary",
        "body",
        "key_points",
        ("url", "is_press_release"),
        ("order", "is_published"),
    ]


@admin.register(BillionaireBlockPage)
class BillionaireBlockPageAdmin(SingletonAdmin):
    inlines = [BillionaireNewsInline, BillionaireResidenceInline]
    fieldsets = [
        (
            "Hero (top of the page)",
            {"fields": ["hero_video", "hero_image", "hero_image_alt", "eyebrow", "title", "tagline"]},
        ),
        (
            "Homepage teaser",
            {
                "fields": ["teaser_label", "teaser_heading", "teaser_text", "teaser_button"],
                "description": "The Billionaire Block band on the homepage, just after the projects section. "
                "It also uses the hero video and images, and the “About the project” figures.",
            },
        ),
        (
            "About the project (just below the hero)",
            {"fields": ["about_label", "about_heading", "about_text", "about_image", "about_image_2", "about_facts"]},
        ),
        (
            "What we are building",
            {
                "fields": [
                    "building_label",
                    "building_heading",
                    "building_text",
                    "building_image",
                    "building_image_2",
                    "building_points",
                    "building_note",
                ]
            },
        ),
        (
            "News (just below the hero)",
            {
                "fields": ["news_label", "news_heading", "news_intro"],
                "description": "The stories are in the “News” tab at the top.",
            },
        ),
        ("Manifesto", {"fields": ["manifesto_heading", "manifesto_text"]}),
        (
            "Architecture & design",
            {
                "fields": [
                    "architecture_label",
                    "architecture_heading",
                    "architecture_text",
                    "architecture_image",
                    ("credit_1_label", "credit_1_value"),
                    ("credit_2_label", "credit_2_value"),
                    ("credit_3_label", "credit_3_value"),
                ]
            },
        ),
        (
            "Section headings",
            {
                "fields": [
                    ("residences_label", "residences_heading"),
                    ("features_label", "features_heading"),
                    "features_intro",
                    ("club_label", "club_heading"),
                    "club_intro",
                    ("amenities_label", "amenities_heading"),
                    "amenities_intro",
                    "amenities_indoor_heading",
                    "amenities_wellness_heading",
                    "amenities_leisure_heading",
                    ("services_label", "services_heading"),
                    "services_intro",
                    ("security_label", "security_heading"),
                    "security_text",
                    "security_image",
                    ("gallery_label", "gallery_heading"),
                    ("specs_label", "specs_heading"),
                    "specs_intro",
                    "specs_image",
                ],
                "description": "The items in each list are under “Billionaire Block content” in the menu.",
            },
        ),
        (
            "Location",
            {"fields": ["location_label", "location_heading", "location_text", "location_note", "map_embed_url"]},
        ),
        ("Developer legacy", {"fields": ["legacy_label", "legacy_heading", "legacy_text"]}),
        (
            "Private viewing form",
            {
                "fields": [
                    "form_label",
                    "form_heading",
                    "form_intro",
                    "viewing_steps",
                    "form_success_title",
                    "form_success_text",
                    "form_note",
                ]
            },
        ),
        ("Brochure", {"fields": ["brochure", "brochure_heading", "brochure_text"]}),
        ("Footer", {"fields": ["rera_number", "footer_disclaimer"]}),
        ("Search engines & sharing", {"fields": ["seo_title", "seo_description"]}),
    ]


@admin.register(BillionaireItem)
class BillionaireItemAdmin(ModelAdmin):
    list_display = ["title", "section", "value", "order", "is_published"]
    list_editable = ["order", "is_published"]
    list_filter = ["section", "is_published"]
    search_fields = ["title", "text"]
    fields = ["section", "title", "value", "text", ("image", "image_alt"), ("order", "is_published")]
