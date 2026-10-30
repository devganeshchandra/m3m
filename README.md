# M3M India website (Django)

The M3M India website and its admin panel, in one Django project. Visitors see
the same site as the previous Next.js version. The content team edits
everything (projects, homepage text, banners, news, gallery, contact details)
from `/admin/`, and every enquiry form saves its lead there.

For the full list of technologies, the database tables and the URLs, see
[docs/TECH_STACK.md](docs/TECH_STACK.md).

## Run it on a new machine (Linux / Ubuntu, macOS, Windows)

Copy or clone the project folder, but **not** `.venv/`. A virtual
environment only works on the machine where it was created. Then:

```bash
cd m3m
chmod +x scripts/*.sh
./scripts/setup.sh                        # installs everything, asks for an admin login
.venv/bin/python manage.py runserver      # Windows Git Bash: .venv/Scripts/python
```

Open http://127.0.0.1:8000/ and http://127.0.0.1:8000/admin/.

On Ubuntu the script installs Python 3.12 with `apt` when needed (it asks for
your sudo password). Ubuntu 24.04 already has it; 22.04 gets it from the
deadsnakes PPA. Running the script again is safe.

**Bring your existing content along** (projects, enquiries, images, admin users):

```bash
./scripts/backup.sh                                  # on the old machine
# copy backups/m3m-backup-….tar.gz to the new machine, then:
./scripts/restore.sh backups/m3m-backup-….tar.gz     # on the new machine
```

Without a backup, the new machine starts with the original starter content.

<details>
<summary>Manual setup without the script</summary>

```bash
python3 -m venv .venv
source .venv/bin/activate            # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env                 # optional for local work
python manage.py migrate
python manage.py seed_content        # loads the current projects, news, gallery…
python manage.py createsuperuser
python manage.py runserver
```
</details>

Run the tests with `python manage.py test`.

## Project layout

| Folder | What's inside |
| --- | --- |
| `config/` | Settings, root URLs, WSGI/ASGI |
| `core/` | Site settings, homepage text, hero banners, simple pages (privacy…), image handling, seed command |
| `projects/` | Projects, which double as landing pages: highlights, floor plans, gallery, brochure, map |
| `content/` | Journey values and stats, press items, media gallery, insights |
| `leads/` | Enquiries from every form, validation, the `/api/enquiries` endpoint |
| `templates/` | All HTML. `home/` is one file per homepage section; `partials/` holds the header, footer and popup |
| `static/css/site.css` | The original stylesheet, compiled once from the old `app/globals.css`. Leave it as is |
| `static/css/django.css` | Django-specific additions (landing-page sections, text pages…) |
| `static/css/pages.css` | Menu pages: banners, collections, timeline, gallery, articles, contact. Add new CSS here |
| `static/js/site.js` | All interactivity: header, smooth scroll, popup, carousel, project discovery, form sending |
| `static/js/validation.js` | Form validation in the browser. **Keep it in step with `leads/validation.py`** |
| `static/vendor/` | GSAP, Lenis and libphonenumber, copied in so no Node.js is needed |
| `seed/images/` | Original images, used only by `seed_content` |
| `scripts/` | `setup.sh`, `install_server.sh`, `update.sh`, `backup.sh`, `restore.sh` |
| `docs/TECH_STACK.md` | Technologies, database tables, URLs |
| `docs/DATABASE.md` | PostgreSQL: connection, leads table, backups, direct access |
| `media/` | Files uploaded through the admin (not committed) |

## How it fits together

- **Pages** are Django templates rendered on the server. There is no build step.
- **Images** uploaded in the admin are downsized to at most 2560px wide. The
  site serves WebP copies at 480/828/1200/1920px through the `{% picture %}`
  tag, which does the job `next/image` did before.
- **Forms** (hero, popup, project discovery) are checked in the browser, then
  posted with `fetch` to `/api/enquiries`. The server checks them again with
  the same rules and saves an `Enquiry`. It also records UTM campaign tags,
  the page URL and the chosen project. Spam is limited by a hidden honeypot
  field and a per-IP hourly limit.
- **Email alerts**: set `LEAD_NOTIFICATION_EMAILS` and the SMTP settings in
  `.env`, and each new enquiry is emailed to the sales team.

## For the content team (admin guide)

Log in at `/admin/`. The left menu is grouped as follows:

- **Enquiries → All enquiries**: every form submission. Filter by status,
  project, source, campaign or date. Change *Status* and *Assigned to*
  straight from the list and press **Save**. To download an Excel file,
  select rows, choose **Export selected to Excel (CSV)** and press **Run**.
- **Projects & landing pages**: add, edit, reorder (*Order*) or hide
  (*Show on site*) a project. Each project page is at `/projects/<slug>`. The
  tabs at the top add highlights, floor plans and gallery images. Those
  sections appear on the page only once they have content.
- **Menu pages (banners & text)**: the banner image, title, intro and SEO
  text of Projects, Our Journey, Media, Insights and Contact. Replace a
  banner by uploading a new image (landscape, at least 1600px wide).
- **Ad landing pages (all content)**: the four pages with their own design,
  Jacob & Co. Residences, The Cullinan, Trump Tower Noida and Billionaire
  Block. Open a page and use the tabs at the top:
  - *Texts*: every heading, paragraph, button label and note, in page order.
    Put `*stars*` around words to show them in italics (the gold words in the
    headings). `{rera}` is replaced by the project's RERA number.
  - *Images*: section backgrounds and other single pictures. Upload a new one
    to replace it.
  - *Lists*: slideshows, amenities, rooms, questions, travel times, menu links,
    the residence choices in the forms… Add, remove, reorder (*Order*) or hide
    (*Show on site*) items. *How each list uses its fields* (at the bottom of
    the page) says what Title, Value, Group, Link etc. mean in each list.
  - *Search engines & sharing*: the Google title and description and the
    WhatsApp/Facebook preview.

  **Ad landing page lists** shows the same list items across all pages, with
  filters by page and list.
- **Billionaire Block page**: the hero video and image, title and tagline, the
  homepage teaser, the private viewing form texts, brochure PDF, RERA number,
  footer disclaimer and SEO of `/billionaire-block`. Everything else on that
  page is under *Ad landing pages → Billionaire Block*. Viewing requests arrive
  with the source *Billionaire Block page*, brochure downloads as *Billionaire
  Block brochure*. Images and the hero video are AI-generated artistic
  impressions: confirm the figures before going live.
- **Projects → Collection**: puts a project in *Now Presenting*, *On the
  Horizon* or *Delivered Landmarks* on the Projects page. **Show on
  homepage** picks the 3 projects shown on the homepage.
- **Homepage text**: every heading and paragraph on the homepage.
- **Insights (articles)**: write articles. Leave a blank line between
  paragraphs and start a line with `## ` for a sub-heading. Tick *Feature*
  to show one at the top of the Insights page.
- **Journey milestones, Videos, FAQs**: the timeline on Our Journey, YouTube
  films on the Media page (paste the YouTube link) and questions on Contact.
- **Hero banners**: add more than one active banner and the homepage turns
  them into a slideshow automatically.
- **Journey values / statistics, Press / news, Media gallery, Insights**:
  the homepage lists. *Order* controls the sequence and *Show on site* hides
  an item without deleting it.
- **Contact & site settings**: phone, WhatsApp number, address, footer
  disclaimer, Google description and the message shown after a form is sent.
- **Pages**: Privacy, Disclaimer and Compliance. A page goes live once it is
  ticked *Published*.
- **Users / Groups**: to give someone limited access, create a group (for
  example "Sales" with only the *Enquiry* permissions, or "Content" with
  everything except users), then add the person to it. Tick *Staff status*
  so they can log in.

## Adding project landing pages

Each project is a landing page at `/projects/<slug>`, built from
`templates/projects/detail.html`. For a campaign, link ads to the project URL
with UTM tags, e.g.
`/projects/m3m-trump-tower-noida?utm_source=google&utm_campaign=launch`.
Enquiries from that visit carry the campaign and project automatically.

Four pages have their own design: Jacob & Co. Residences, The Cullinan, Trump
Tower Noida and Billionaire Block. Their content is not in the templates but in
the admin (**Ad landing pages**). Each page's text slots, image slots and lists,
with their starting content, are described in `projects/landing_pages/<page>.py`;
`projects/landing.py` creates the rows during `migrate` and never overwrites
what the content team has edited.

To give another project its own design:

1. Add `templates/projects/landing/<project-slug>.html` and read its content
   from `t.<key>` (texts, `|em` for *italics*), `imgs.<key>` (images, `|src:<width>`)
   and `lists.<key>` (lists).
2. Add `projects/landing_pages/<name>.py` describing those slots, and list it in
   `PAGES` in `projects/landing.py`.
3. Add a migration that runs `landing.seed(apps)` (copy
   `projects/migrations/0018_landing_pages_content.py`).

The project then uses its new page automatically. The models, the enquiry popup
and the lead capture are reused as they are.

## Put it online on an Ubuntu server

Steps for Ubuntu 22.04 / 24.04. Point your domain's DNS to the server first.

```bash
sudo apt-get update && sudo apt-get install -y git
git clone <your-repo-url> m3m && cd m3m        # or copy the folder (without .venv)
chmod +x scripts/*.sh
./scripts/setup.sh --production --domain www.m3mindia.com
sudo ./scripts/install_server.sh www.m3mindia.com   # Gunicorn service + Nginx + HTTPS
```

This gives you:
- a `m3m` systemd service that runs Gunicorn on `127.0.0.1:8000`, starts on
  boot and restarts if it crashes;
- Nginx on ports 80/443 in front of it, accepting uploads up to 30 MB;
- a free Let's Encrypt HTTPS certificate, if you answer yes.

Day to day:

```bash
sudo systemctl status m3m        # is it running?
sudo journalctl -u m3m -f        # live logs
git pull && ./scripts/update.sh  # deploy new code
./scripts/backup.sh              # backup (e.g. nightly via cron)
```

Edit `.env` for email alerts (`LEAD_NOTIFICATION_EMAILS`, `EMAIL_HOST`…) or
PostgreSQL, then run `sudo systemctl restart m3m`.
`.venv/bin/python manage.py check --deploy` lists any production settings
still missing.

For a nightly backup at 2 AM, add this line with `crontab -e`:

```
0 2 * * * cd /home/<user>/m3m && ./scripts/backup.sh >/dev/null 2>&1
```
