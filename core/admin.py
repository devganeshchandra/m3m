from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group, User
from django.shortcuts import redirect
from django.urls import reverse
from unfold.admin import ModelAdmin
from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm

from core.models import FAQ, HeroBanner, HomePage, InnerPage, Page, SiteSettings

admin.site.site_header = "M3M India"
admin.site.site_title = "M3M India Admin"
admin.site.index_title = "Website content & enquiries"

admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm


@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass


class SingletonAdmin(ModelAdmin):
    """Skip the list page and open the single settings form directly."""

    def has_add_permission(self, request):
        return not self.model.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False

    def changelist_view(self, request, extra_context=None):
        obj = self.model.load()
        opts = self.model._meta
        return redirect(reverse(f"admin:{opts.app_label}_{opts.model_name}_change", args=[obj.pk]))


@admin.register(SiteSettings)
class SiteSettingsAdmin(SingletonAdmin):
    fieldsets = [
        ("Phone & WhatsApp", {"fields": ["phone_display", "phone_dial", "phone_international", "whatsapp_number"]}),
        ("Email, hours & map (Contact page)", {"fields": ["email", "office_hours", "map_embed_url"]}),
        (
            "Corporate office address",
            {"fields": ["address_line_1", "address_line_2", "street_address", "city", "postal_code"]},
        ),
        ("Search engines & sharing", {"fields": ["site_name", "default_title", "meta_description", "share_image"]}),
        ("Enquiry forms", {"fields": ["enquiry_success_message"]}),
        ("Footer", {"fields": ["footer_disclaimer", "footer_note"]}),
    ]


@admin.register(HomePage)
class HomePageAdmin(SingletonAdmin):
    fieldsets = [
        (
            "Hero (top of the page)",
            {
                "fields": [
                    "hero_eyebrow",
                    ("hero_headline_line_1", "hero_headline_line_2"),
                    "hero_intro",
                    "hero_link_label",
                    ("hero_caption_left", "hero_caption_right"),
                    ("hero_form_title", "hero_form_intro"),
                ],
                "description": "Banner images are managed under “Hero banners”.",
            },
        ),
        (
            "Projects section",
            {"fields": ["projects_label", ("projects_title_line_1", "projects_title_line_2"), "projects_intro"]},
        ),
        (
            "Our Journey section",
            {
                "fields": [
                    "journey_label",
                    ("journey_title_line_1", "journey_title_line_2"),
                    "journey_summary",
                    ("journey_link_label", "journey_link_url"),
                    "journey_stats_note",
                ],
                "description": "Values and numbers are managed under “Journey values” and “Journey statistics”.",
            },
        ),
        ("News section", {"fields": ["news_label", ("news_title_line_1", "news_title_line_2"), "news_intro"]}),
        ("Media gallery section", {"fields": ["media_label", ("media_title_line_1", "media_title_line_2"), "media_intro"]}),
        ("Insights section", {"fields": ["insights_label", "insights_title", "insights_intro"]}),
        ("Project discovery section", {"fields": ["guided_label", "guided_title", "guided_intro"]}),
        (
            "Contact section",
            {
                "fields": [
                    "contact_label",
                    ("contact_title_line_1", "contact_title_line_2"),
                    "contact_intro",
                    "contact_button_label",
                    "contact_footer_tagline",
                ]
            },
        ),
    ]


@admin.register(HeroBanner)
class HeroBannerAdmin(ModelAdmin):
    list_display = ["__str__", "order", "is_active"]
    list_editable = ["order", "is_active"]


@admin.register(Page)
class PageAdmin(ModelAdmin):
    list_display = ["title", "slug", "is_published", "updated_at"]
    list_editable = ["is_published"]
    prepopulated_fields = {"slug": ["title"]}
    search_fields = ["title", "body"]


@admin.register(InnerPage)
class InnerPageAdmin(ModelAdmin):
    list_display = ["__str__", "title", "updated_at"]

    HERO = ("Banner", {"fields": ["banner", "banner_alt", "eyebrow", "title", "title_emphasis", "intro"]})
    INTRO = ("Introduction section", {"fields": ["intro_label", "intro_heading", "intro_text"]})
    SEO = ("Search engines", {"fields": ["seo_title", "seo_description"], "classes": ["collapse"]})
    EXTRA = {
        InnerPage.Key.PROJECTS: [
            (
                "Collections",
                {
                    "fields": ["delivered_text", "current_text", "upcoming_text"],
                    "description": "Choose each project's collection on the project itself.",
                },
            )
        ],
        InnerPage.Key.JOURNEY: [("Quotation", {"fields": ["quote_text", "quote_attribution"]})],
    }

    def get_fieldsets(self, request, obj=None):
        extra = self.EXTRA.get(obj.key, []) if obj else []
        return [self.HERO, self.INTRO, *extra, self.SEO]

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(FAQ)
class FAQAdmin(ModelAdmin):
    list_display = ["question", "order", "is_published"]
    list_editable = ["order", "is_published"]
