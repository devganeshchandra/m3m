from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from content.models import Insight
from core.models import InnerPage, Page
from projects.models import Project


class HomeSitemap(Sitemap):
    priority = 1.0
    changefreq = "weekly"

    def items(self):
        return ["core:home"]

    def location(self, item):
        return reverse(item)


class BillionaireBlockSitemap(Sitemap):
    priority = 0.9
    changefreq = "weekly"

    def items(self):
        return ["projects:billionaire_block"]

    def location(self, item):
        return reverse(item)


class MenuPageSitemap(Sitemap):
    priority = 0.9
    changefreq = "weekly"

    def items(self):
        return InnerPage.objects.all()

    def lastmod(self, obj):
        return obj.updated_at


class InsightSitemap(Sitemap):
    priority = 0.6
    changefreq = "monthly"

    def items(self):
        return Insight.objects.filter(is_published=True)

    def lastmod(self, obj):
        return obj.published_on


class ProjectSitemap(Sitemap):
    priority = 0.8
    changefreq = "weekly"

    def items(self):
        return Project.objects.published()

    def lastmod(self, obj):
        return obj.updated_at


class PageSitemap(Sitemap):
    priority = 0.3

    def items(self):
        return Page.objects.filter(is_published=True)

    def lastmod(self, obj):
        return obj.updated_at


sitemaps = {
    "home": HomeSitemap,
    "billionaire-block": BillionaireBlockSitemap,
    "menu": MenuPageSitemap,
    "projects": ProjectSitemap,
    "insights": InsightSitemap,
    "pages": PageSitemap,
}
