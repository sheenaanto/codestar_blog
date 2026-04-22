# CodeStar Blog

CodeStar Blog is a Django blog application with authentication, post publishing, comment moderation, and an About page with a collaboration request form.

## What This Project Includes

- Post listing with pagination
- Draft and published post workflow
- Post detail pages with comments
- Comment create/edit/delete for signed-in users
- Admin moderation for comments
- About page content managed from the database
- Collaboration request form
- Cloudinary image hosting for posts and profile images
- Django Allauth authentication flow

## Tech Stack

- Python 3.12
- Django 4.2
- PostgreSQL (production)
- SQLite (automatically used during tests)
- Cloudinary + dj3-cloudinary-storage
- Django Summernote editor
- Django Crispy Forms with Bootstrap 5
- Gunicorn + WhiteNoise

## Quick Start (Local Development)

### 1. Clone and enter the project

```bash
git clone <your-repository-url>
cd codestar_blog
```

### 2. Create and activate a virtual environment

Windows (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add environment variables

Create an env.py file in the project root with:

```python
import os

os.environ.setdefault("SECRET_KEY", "your-secret-key")
os.environ.setdefault("DATABASE_URL", "sqlite:///db.sqlite3")
os.environ.setdefault("CLOUDINARY_URL", "your-cloudinary-url")
```

Notes:

- DATABASE_URL is required by settings.py
- In production, use a PostgreSQL URL for DATABASE_URL
- Keep real values out of version control

### 5. Apply migrations

```bash
python manage.py migrate
```

### 6. Create an admin user

```bash
python manage.py createsuperuser
```

### 7. Start the server

```bash
python manage.py runserver
```

Open:

- Home page: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/
- About page: http://127.0.0.1:8000/about/

## Main URLs

- / -> blog index
- /<slug>/ -> post detail
- /accounts/ -> authentication routes (Allauth)
- /about/ -> About + collaboration form
- /admin/ -> Django admin

## Content Management Workflow

### Publish a blog post

1. Log in to /admin/
2. Open Posts
3. Add title, slug, content, featured image, excerpt, and status
4. Set status to Published to show on the site

### Moderate comments

1. Open Comments in /admin/
2. Approve comments you want to display publicly

## Testing

Run all tests:

```bash
python manage.py test
```

Run app-specific tests:

```bash
python manage.py test blog
python manage.py test about
```

## Deployment Notes

- Procfile is configured to run Gunicorn:

```text
web: gunicorn codestar.wsgi
```

- runtime.txt pins Python:

```text
python-3.12.3
```

- Required environment variables in deployment:
  - SECRET_KEY
  - DATABASE_URL
  - CLOUDINARY_URL

## Project Structure (High Level)

```text
about/       About page and collaboration request app
blog/        Blog posts, comments, and related views/forms
codestar/    Project settings and root URL configuration
templates/   Shared templates and allauth templates
static/      Source static assets
staticfiles/ Collected static assets
```

## License

This project was created as part of the Code Institute learning curriculum.
