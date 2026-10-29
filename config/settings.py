"""
Django settings for the M3M India website.

Everything environment-specific is read from environment variables (or a
local `.env` file). See `.env.example` for the full list.
"""

import os
from pathlib import Path

from django.templatetags.static import static
from django.urls import reverse_lazy
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")


def env_bool(name, default=False):
    return os.environ.get(name, str(default)).strip().lower() in {"1", "true", "yes", "on"}


def env_list(name, default=""):
    return [item.strip() for item in os.environ.get(name, default).split(",") if item.strip()]


DEBUG = env_bool("DJANGO_DEBUG", True)
SECRET_KEY = os.environ.get(
    "DJANGO_SECRET_KEY",
    "django-insecure-local-development-key-change-me" if DEBUG else "",
)
if not SECRET_KEY:
    raise RuntimeError("DJANGO_SECRET_KEY must be set when DJANGO_DEBUG is off.")

ALLOWED_HOSTS = env_list("DJANGO_ALLOWED_HOSTS", "localhost,127.0.0.1")
CSRF_TRUSTED_ORIGINS = env_list("DJANGO_CSRF_TRUSTED_ORIGINS")
SITE_URL = os.environ.get("SITE_URL", "https://www.m3mindia.com").rstrip("/")

INSTALLED_APPS = [
    "unfold",
    "unfold.contrib.filters",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    # WhiteNoise serves static files in development too, with headers that stop
    # browsers reusing an old copy of the CSS/JS after an edit.
    "whitenoise.runserver_nostatic",
    "django.contrib.staticfiles",
    "django.contrib.sitemaps",
    "core",
    "projects",
    "content",
    "leads",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "core.context_processors.site",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

# Database: SQLite by default; set DB_ENGINE=postgres (and install
# "psycopg[binary]") to use PostgreSQL in production.
if os.environ.get("DB_ENGINE", "sqlite").lower() in {"postgres", "postgresql"}:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.environ.get("DB_NAME", "m3m"),
            "USER": os.environ.get("DB_USER", "m3m"),
            "PASSWORD": os.environ.get("DB_PASSWORD", ""),
            "HOST": os.environ.get("DB_HOST", "localhost"),
            "PORT": os.environ.get("DB_PORT", "5432"),
            "CONN_MAX_AGE": 60,
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LANGUAGE_CODE = "en-in"
TIME_ZONE = "Asia/Kolkata"
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

STORAGES = {
    "default": {"BACKEND": "django.core.files.storage.FileSystemStorage"},
    "staticfiles": {
        "BACKEND": (
            "django.contrib.staticfiles.storage.StaticFilesStorage"
            if DEBUG
            else "whitenoise.storage.CompressedManifestStaticFilesStorage"
        )
    },
}

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "m3m",
    }
}

# Uploaded images larger than this are resized on save, and the site serves
# WebP renditions at these widths (similar to next/image).
IMAGE_MAX_UPLOAD_WIDTH = 2560
IMAGE_RENDITION_WIDTHS = (480, 828, 1200, 1920)

# Lead notifications: comma-separated recipients. Leave empty to only store
# enquiries in the admin.
LEAD_NOTIFICATION_EMAILS = env_list("LEAD_NOTIFICATION_EMAILS")
LEAD_RATE_LIMIT_PER_HOUR = int(os.environ.get("LEAD_RATE_LIMIT_PER_HOUR", "20"))

EMAIL_BACKEND = os.environ.get(
    "EMAIL_BACKEND",
    "django.core.mail.backends.console.EmailBackend"
    if DEBUG
    else "django.core.mail.backends.smtp.EmailBackend",
)
EMAIL_HOST = os.environ.get("EMAIL_HOST", "localhost")
EMAIL_PORT = int(os.environ.get("EMAIL_PORT", "587"))
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER", "")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD", "")
EMAIL_USE_TLS = env_bool("EMAIL_USE_TLS", True)
DEFAULT_FROM_EMAIL = os.environ.get("DEFAULT_FROM_EMAIL", "M3M India <no-reply@m3mindia.com>")

if not DEBUG:
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
    SECURE_SSL_REDIRECT = env_bool("DJANGO_SECURE_SSL_REDIRECT", True)
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_HSTS_SECONDS = int(os.environ.get("DJANGO_HSTS_SECONDS", "0"))
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_REFERRER_POLICY = "strict-origin-when-cross-origin"

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {"console": {"class": "logging.StreamHandler"}},
    "root": {"handlers": ["console"], "level": "INFO"},
}

UNFOLD = {
    "SITE_TITLE": "M3M India Admin",
    "SITE_HEADER": "M3M India",
    "SITE_SUBHEADER": "Website content & enquiries",
    "SITE_URL": "/",
    "SITE_SYMBOL": "apartment",
    "SITE_FAVICONS": [
        {"rel": "icon", "type": "image/png", "href": lambda request: static("images/logo/m3m-logo.png")},
    ],
    "SHOW_HISTORY": True,
    "SHOW_VIEW_ON_SITE": True,
    "COLORS": {
        "primary": {
            "50": "oklch(97% .012 85)",
            "100": "oklch(94% .03 85)",
            "200": "oklch(89% .06 83)",
            "300": "oklch(82% .09 80)",
            "400": "oklch(74% .11 78)",
            "500": "oklch(68% .12 76)",
            "600": "oklch(60% .115 74)",
            "700": "oklch(51% .1 72)",
            "800": "oklch(43% .08 70)",
            "900": "oklch(36% .065 68)",
            "950": "oklch(26% .05 66)",
        },
    },
    "SIDEBAR": {
        "show_search": True,
        "show_all_applications": True,
        "navigation": [
            {
                "title": "Enquiries",
                "items": [
                    {"title": "All enquiries", "icon": "inbox", "link": reverse_lazy("admin:leads_enquiry_changelist")},
                ],
            },
            {
                "title": "Projects",
                "items": [
                    {"title": "Projects & landing pages", "icon": "apartment", "link": reverse_lazy("admin:projects_project_changelist")},
                    {"title": "Ad landing pages (all content)", "icon": "campaign", "link": reverse_lazy("admin:projects_landingpage_changelist")},
                    {"title": "Ad landing page lists", "icon": "format_list_bulleted", "link": reverse_lazy("admin:projects_landingitem_changelist")},
                    {"title": "Billionaire Block page", "icon": "diamond", "link": reverse_lazy("admin:projects_billionaireblockpage_changelist")},
                ],
            },
            {
                "title": "Website content",
                "items": [
                    {"title": "Homepage text", "icon": "home", "link": reverse_lazy("admin:core_homepage_changelist")},
                    {"title": "Menu pages (banners & text)", "icon": "web", "link": reverse_lazy("admin:core_innerpage_changelist")},
                    {"title": "Hero banners", "icon": "photo_library", "link": reverse_lazy("admin:core_herobanner_changelist")},
                    {"title": "Journey values", "icon": "timeline", "link": reverse_lazy("admin:content_journeyprinciple_changelist")},
                    {"title": "Journey statistics", "icon": "bar_chart", "link": reverse_lazy("admin:content_journeystat_changelist")},
                    {"title": "Journey milestones", "icon": "flag", "link": reverse_lazy("admin:content_milestone_changelist")},
                    {"title": "Press / news", "icon": "newspaper", "link": reverse_lazy("admin:content_pressitem_changelist")},
                    {"title": "Publications (news logos)", "icon": "verified", "link": reverse_lazy("admin:content_publication_changelist")},
                    {"title": "Media gallery", "icon": "collections", "link": reverse_lazy("admin:content_mediaimage_changelist")},
                    {"title": "Videos", "icon": "smart_display", "link": reverse_lazy("admin:content_video_changelist")},
                    {"title": "Insights (articles)", "icon": "lightbulb", "link": reverse_lazy("admin:content_insight_changelist")},
                    {"title": "FAQs (Contact page)", "icon": "help", "link": reverse_lazy("admin:core_faq_changelist")},
                ],
            },
            {
                "title": "Site",
                "items": [
                    {"title": "Contact & site settings", "icon": "settings", "link": reverse_lazy("admin:core_sitesettings_changelist")},
                    {"title": "Pages (privacy, disclaimer…)", "icon": "description", "link": reverse_lazy("admin:core_page_changelist")},
                    {"title": "Users", "icon": "person", "link": reverse_lazy("admin:auth_user_changelist")},
                    {"title": "Groups & permissions", "icon": "group", "link": reverse_lazy("admin:auth_group_changelist")},
                ],
            },
        ],
    },
}
