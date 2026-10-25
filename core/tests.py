import shutil
import tempfile
from io import BytesIO

from django.contrib.auth.models import User
from django.core.cache import cache
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.management import call_command
from django.test import TestCase, override_settings
from PIL import Image

from content.models import Insight, Video
from core.models import HeroBanner, HomePage, InnerPage, Page, SiteSettings
from projects.models import BillionaireBlockPage, BillionaireItem, Project

MEDIA_ROOT = tempfile.mkdtemp()


@override_settings(MEDIA_ROOT=MEDIA_ROOT)
class SiteTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        call_command("seed_content", verbosity=0)

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        shutil.rmtree(MEDIA_ROOT, ignore_errors=True)

    def setUp(self):
        cache.clear()

    def test_homepage_renders_seeded_content(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "A legacy of")
        self.assertContains(response, "M3M Trump Tower Noida")
        self.assertContains(response, "Moneycontrol")
        self.assertContains(response, "Wellness woven into the everyday")
        self.assertContains(response, 'class="project-card"', count=3)
        self.assertContains(response, "Explore all 9 projects")
        # Live figures beside the section headings, the journey card and the single-screen finder.
        self.assertContains(response, "<strong>9</strong><span>Addresses</span>", html=False)
        self.assertContains(response, "M3M India at a glance")
        self.assertContains(response, "Projects delivered")
        self.assertContains(response, 'class="finder-project"', count=9)
        self.assertContains(response, "Send me my M3M edit")

    def test_homepage_text_is_editable(self):
        page = HomePage.load()
        page.hero_headline_line_1 = "A brand new"
        page.save()
        self.assertContains(self.client.get("/"), "A brand new")

    def test_contact_settings_are_used_everywhere(self):
        settings = SiteSettings.load()
        settings.phone_display = "1800 000 0000"
        settings.whatsapp_number = "911234567890"
        settings.save()
        response = self.client.get("/")
        self.assertContains(response, "1800 000 0000")
        self.assertContains(response, "https://wa.me/911234567890")

    def test_project_page(self):
        response = self.client.get("/projects/m3m-trump-tower-noida")
        self.assertContains(response, "UPRERAPRJ794824/10/2025")
        self.assertContains(response, "<title>M3M Trump Tower Noida | M3M India</title>", html=False)

    def test_unpublished_project_is_hidden(self):
        Project.objects.filter(slug="m3m-trump-tower-noida").update(is_published=False)
        self.assertEqual(self.client.get("/projects/m3m-trump-tower-noida").status_code, 404)
        self.assertNotContains(self.client.get("/"), "M3M Trump Tower Noida")

    def test_project_landing_sections(self):
        project = Project.objects.get(slug="m3m-trump-tower-noida")
        project.highlights.create(title="Golf course views")
        project.configurations.create(unit_type="4 BHK", size="4,800 sq. ft.")
        response = self.client.get(project.get_absolute_url())
        self.assertContains(response, "Golf course views")
        self.assertContains(response, "4,800 sq. ft.")
        self.assertContains(response, "Price on request")

    def test_pages(self):
        self.assertEqual(self.client.get("/disclaimer").status_code, 200)
        self.assertEqual(self.client.get("/privacy").status_code, 404)
        Page.objects.filter(slug="privacy").update(is_published=True)
        self.assertEqual(self.client.get("/privacy").status_code, 200)

    def test_seo_files(self):
        self.assertContains(self.client.get("/sitemap.xml"), "/projects/m3m-trump-tower-noida")
        self.assertContains(self.client.get("/sitemap.xml"), "/billionaire-block")
        self.assertContains(self.client.get("/robots.txt"), "Sitemap:")

    def test_admin_screens_load(self):
        admin = User.objects.create_superuser("admin", "a@example.com", "pass")
        self.client.force_login(admin)
        for url in [
            "/admin/",
            "/admin/leads/enquiry/",
            "/admin/projects/project/",
            "/admin/projects/project/add/",
            f"/admin/projects/project/{Project.objects.first().pk}/change/",
            "/admin/core/homepage/1/change/",
            "/admin/projects/billionaireblockpage/1/change/",
            "/admin/projects/billionaireitem/",
            "/admin/core/sitesettings/1/change/",
            "/admin/core/herobanner/",
            "/admin/core/page/",
            "/admin/content/pressitem/",
            "/admin/content/mediaimage/",
            "/admin/content/insight/",
            "/admin/content/journeyprinciple/",
            "/admin/content/journeystat/",
            "/admin/content/milestone/",
            "/admin/content/video/",
            "/admin/core/faq/",
            "/admin/core/innerpage/",
            f"/admin/core/innerpage/{InnerPage.objects.get(key='projects').pk}/change/",
            f"/admin/core/innerpage/{InnerPage.objects.get(key='journey').pk}/change/",
            f"/admin/content/insight/{Insight.objects.first().pk}/change/",
        ]:
            self.assertEqual(self.client.get(url).status_code, 200, url)

    def test_billionaire_block_page(self):
        response = self.client.get("/billionaire-block")
        self.assertContains(response, "<title>Billionaire Block by M3M | Residences by invitation only</title>", html=False)
        self.assertContains(response, '"@type": "RealEstateListing"', html=False)
        self.assertContains(response, "Some addresses are bought. This one is earned.")
        self.assertContains(response, 'data-count="12,000+"', html=False)
        self.assertContains(response, "Sky Villas")
        self.assertContains(response, 'class="bb-club__card"', count=11)
        self.assertContains(response, "Biometric &amp; facial recognition")
        self.assertContains(response, "Indira Gandhi International Airport")
        self.assertContains(response, "data-bb-lightbox=", count=13)
        # Amenities: three groups, every amenity named, photos only where one is uploaded.
        self.assertContains(response, 'class="bb-amenities__group"', count=3)
        self.assertContains(response, "Bonfire court")
        self.assertContains(response, "<figcaption>Bowling alley</figcaption>", html=False)
        self.assertContains(response, "Air conditioning")
        self.assertContains(response, "Request Invitation")
        self.assertContains(response, 'name="source" value="billionaire"', html=False)
        self.assertContains(response, 'name="source" value="brochure"', html=False)
        self.assertContains(response, "billionaire-block/hero")
        # Published news cards with their popup content and source links.
        self.assertContains(response, 'class="bb-news__card"', count=4)
        self.assertContains(response, "Gurugram residences priced from about ₹15 crore")
        self.assertContains(response, "https://luxe.outlookindia.com/", html=False)
        self.assertContains(response, "a paid press release", count=1)

    def test_billionaire_block_is_highlighted_in_the_site_menu(self):
        response = self.client.get("/")
        self.assertContains(response, "desktop-nav__link--featured", html=False)

    def test_homepage_teases_billionaire_block(self):
        response = self.client.get("/")
        self.assertContains(response, 'class="bbt"', html=False)
        self.assertContains(response, "Something extraordinary is rising.")
        self.assertContains(response, 'href="/billionaire-block"', html=False)
        self.assertContains(response, "/billionaire-block#private-viewing", html=False)
        # The light projects section separates the dark banner from the dark teaser.
        html = response.content.decode()
        self.assertLess(html.index('class="phase-one-hero"'), html.index('id="projects"'))
        self.assertLess(html.index('id="projects"'), html.index('class="bbt"'))

    def test_billionaire_block_is_editable(self):
        page = BillionaireBlockPage.load()
        page.tagline = "A new horizon."
        page.save()
        BillionaireItem.objects.filter(title="Golf simulator").update(is_published=False)
        response = self.client.get("/billionaire-block")
        self.assertContains(response, "A new horizon.")
        self.assertNotContains(response, "Golf simulator")

    def test_large_upload_is_downsized(self):
        admin = User.objects.create_superuser("admin", "a@example.com", "pass")
        self.client.force_login(admin)
        buffer = BytesIO()
        Image.new("RGB", (4000, 2000), "navy").save(buffer, "JPEG")
        upload = SimpleUploadedFile("huge.jpg", buffer.getvalue(), content_type="image/jpeg")
        response = self.client.post("/admin/core/herobanner/add/", {"image": upload, "order": 1, "is_active": "on"})
        self.assertEqual(response.status_code, 302)
        banner = HeroBanner.objects.order_by("-pk").first()
        self.assertEqual(banner.image.width, 2560)


@override_settings(MEDIA_ROOT=MEDIA_ROOT)
class MenuPageTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        call_command("seed_content", verbosity=0)

    def setUp(self):
        cache.clear()

    def test_every_menu_page_renders_with_its_banner(self):
        for page in InnerPage.objects.all():
            response = self.client.get(page.get_absolute_url())
            self.assertEqual(response.status_code, 200, page.key)
            self.assertContains(response, page.title)
            self.assertContains(response, 'class="inner-hero"')
            self.assertContains(response, 'aria-current="page"')

    def test_projects_page_groups_collections(self):
        response = self.client.get("/projects")
        for name in ("Now Presenting", "On the Horizon", "Delivered Landmarks"):
            self.assertContains(response, name)
        self.assertContains(response, 'class="project-card"', count=9)

    def test_project_status_moves_it_between_collections(self):
        Project.objects.update(status=Project.Status.CURRENT)
        response = self.client.get("/projects")
        self.assertContains(response, "New addresses for this collection will be announced soon.", count=2)

    def test_homepage_featured_projects(self):
        Project.objects.update(is_featured=False)
        Project.objects.filter(slug="smartworld-noida-commercial").update(is_featured=True)
        featured = Project.objects.for_homepage()
        self.assertEqual(featured[0].slug, "smartworld-noida-commercial")
        self.assertEqual(len(featured), 3)

    def test_insight_article(self):
        insight = Insight.objects.get(slug="reading-a-rera-registration-a-buyers-checklist")
        response = self.client.get(insight.get_absolute_url())
        self.assertContains(response, "<h2>Understand carpet area</h2>", html=True)
        self.assertContains(response, "More <em>insights.</em>", html=True)

    def test_media_page_lists_gallery_and_press(self):
        response = self.client.get("/media-centre")
        self.assertContains(response, 'class="masonry__item"', count=13)
        self.assertContains(response, "Moneycontrol")
        self.assertNotContains(response, 'id="films"')
        Video.objects.create(title="Walkthrough", youtube_url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        self.assertContains(self.client.get("/media-centre"), "dQw4w9WgXcQ")

    def test_contact_page(self):
        response = self.client.get("/contact")
        self.assertContains(response, 'value="contact"')
        self.assertContains(response, "Frequently")

    def test_video_id_parsing(self):
        for url in ["https://youtu.be/dQw4w9WgXcQ", "https://www.youtube.com/watch?v=dQw4w9WgXcQ&t=3",
                    "https://www.youtube.com/shorts/dQw4w9WgXcQ"]:
            self.assertEqual(Video(youtube_url=url).youtube_id, "dQw4w9WgXcQ")


@override_settings(MEDIA_ROOT=MEDIA_ROOT)
class PressTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        call_command("seed_content", verbosity=0)

    def test_news_cards_show_publication_logos(self):
        from content.models import Publication

        response = self.client.get("/")
        for publication in Publication.objects.filter(items__is_published=True).distinct():
            self.assertTrue(publication.logo, publication.name)
            self.assertContains(response, publication.logo.url)
        self.assertContains(response, "As featured in")
        self.assertContains(response, 'class="press-card press-card--publication"', count=3)
        self.assertContains(self.client.get("/media-centre"), "Read on Outlook Luxe")
