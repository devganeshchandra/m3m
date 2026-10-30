# Database

The website stores everything in **PostgreSQL**: every page text, project, landing page, article, setting,
admin user, and every **lead** (enquiry) from every form. Pictures, brochures and floor plans are files in the
`media/` folder; the database stores where each one is.

## Connection settings

The site reads them from `.env` in the project folder (never commit it; it is in `.gitignore`):

```
DB_ENGINE=postgres
DB_NAME=m3m
DB_USER=m3m
DB_PASSWORD=…            # a long random password
DB_HOST=localhost        # or the database server's address
DB_PORT=5432
DB_SSLMODE=prefer        # "require" when the database is on another server
DB_CONN_MAX_AGE=60       # seconds a connection is reused
```

The website logs in as the `m3m` user, which owns only the `m3m` database. The PostgreSQL administrator
account (`postgres`) is for maintenance only; the website never uses it.

## The leads table

Leads are in the table **`leads_enquiry`** (admin: *Enquiries*). One row per lead:

| Column | What it holds |
| --- | --- |
| `id` | Lead number |
| `created_at`, `updated_at` | When it arrived, when it last changed |
| `source` | Which form: `landing`, `popup`, `hero`, `contact`, `billionaire`, `brochure`… |
| `project_id` | The project it is about (→ `projects_project`) |
| `name`, `phone`, `email` | The visitor; the phone is stored in international format (+91…) |
| `call_time`, `interest`, `residency` | Their choices on the form |
| `message` | What they asked for (e.g. “Requested: Get the price list · Interested in: 4 BHK”) |
| `consent` | Whether they ticked the consent box |
| `page_url`, `utm_source` … `utm_content` | The page and the ad campaign they came from |
| `ip_address`, `user_agent` | Their connection, for spotting spam |
| `status`, `assigned_to_id`, `notes` | The sales team’s follow-up (new → contacted → … → booked) |

Indexes keep the newest-first list, the status and source filters, and look-ups by phone and email fast as the
table grows. On ad landing pages, the same phone number enquiring about the same project within a day is added
to the existing lead instead of creating a duplicate.

Everyday use is in the admin (**Enquiries**): filter, search, assign, add notes, and **Export selected to
Excel (CSV)**.

## Connecting to the database directly

- **pgAdmin** (free, pgadmin.org) or **DBeaver**: new connection → host, port 5432, database `m3m`, user `m3m`
  and the password from `.env`.
- **Command line:** `psql -h localhost -U m3m -d m3m`, or from the project folder:
  `.venv/bin/python manage.py dbshell` (Windows: `.venv\Scripts\python`).

Read data there freely, but **change data in the admin**: the admin checks every value; direct edits do not.

Useful queries:

```sql
-- Leads of the last 7 days, newest first
SELECT created_at, name, phone, email, source, status FROM leads_enquiry
WHERE created_at > now() - interval '7 days' ORDER BY created_at DESC;

-- Leads per project
SELECT p.name, count(*) FROM leads_enquiry e LEFT JOIN projects_project p ON p.id = e.project_id
GROUP BY p.name ORDER BY count(*) DESC;
```

## Schema changes

The schema comes from the code (Django migrations). After every code update run:

```
.venv/bin/python manage.py migrate
```

It creates or changes tables and indexes and never touches content the team has edited. Do not create or alter
tables by hand.

## Backups

```
./scripts/backup.sh
```

saves one file in `backups/` with the whole database (`data.json`, which loads into any database, and
`database.dump`, PostgreSQL’s own format), plus all uploaded files. Run it nightly (see README) and copy the
files somewhere off the server. Restore with `./scripts/restore.sh backups/<file>.tar.gz`; it replaces
everything currently in the database.

`database.dump` can also be restored directly: `pg_restore --clean --no-owner -h localhost -U m3m -d m3m database.dump`.

## Setting up PostgreSQL on a new server

`./scripts/setup.sh --production --domain …` does this automatically on Ubuntu/Debian. By hand:

```
sudo apt-get install -y postgresql
sudo -u postgres psql -c "CREATE ROLE m3m LOGIN PASSWORD 'a-long-random-password';"
sudo -u postgres psql -c "CREATE DATABASE m3m OWNER m3m ENCODING 'UTF8' TEMPLATE template0;"
```

then put the password in `.env`, run `migrate`, and restore the latest backup.

With a managed database (AWS RDS, Azure, Google Cloud SQL, DigitalOcean…), create the `m3m` database and user in
its console, set `DB_HOST` to its address and `DB_SSLMODE=require`.

## Security

- Keep port 5432 closed to the internet: only the website server connects to it.
- Use long random passwords and keep them in a password manager, not in email or chat.
- `.env`, `backups/` and `media/` hold customers’ details: never commit them or share them publicly.
