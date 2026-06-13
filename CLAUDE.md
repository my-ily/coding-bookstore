# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Coding Bookstore — a Django 5.2 web app that browses programming books via the Google Books API, with user auth and a personal wishlist stored in PostgreSQL.

## Environment Setup

Copy `.env.example` to `.env` and fill in values. The app requires PostgreSQL; the Docker Compose file spins up a local instance:

```bash
docker-compose up -d          # start Postgres (port 5433) + pgAdmin (port 5050)
cp .env.example .env          # then edit .env with real values
source myenv/bin/activate     # activate the local virtualenv
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Key `.env` variables:
- `GOOGLE_BOOKS_API_KEY` — optional; without it, requests still work but may hit rate limits
- `DB_HOST=127.0.0.1`, `DB_PORT=5433` (matches docker-compose)

## Common Commands

```bash
python manage.py runserver          # dev server
python manage.py migrate            # apply migrations
python manage.py makemigrations     # generate migration after model changes
python manage.py createsuperuser    # create admin user
python manage.py test               # run tests
python manage.py test Bookstore1    # run app-specific tests
python manage.py collectstatic      # gather static files (needed before prod deploy)
```

Production uses gunicorn: `gunicorn config.wsgi` (see `Procfile`).

## Architecture

```
config/          — Django project settings, root URL conf, wsgi/asgi
Bookstore1/      — sole Django app: models, views, admin, migrations
  templates/     — all HTML templates (no per-app subdirectory)
staticfiles/     — collected static output (WhiteNoise serves this)
```

**Request flow:** `config/urls.py` → `Bookstore1/views.py` → templates in `Bookstore1/templates/`

**External data:** Books come from the Google Books API (`https://www.googleapis.com/books/v1/volumes`). `fetch_books()` and `book_detail()` in `views.py` call this API directly on each request — there is no local caching. The helper `_google_books_params()` injects the API key when set.

**Database:** Only one model — `Wishlist` (user FK + Google Books `book_id` + denormalized metadata). The `Wishlist.objects.get_or_create` pattern prevents duplicates. Django's built-in `User` model handles auth.

**Auth:** Custom login/logout views (`auth_login`, `custom_logout`). Registration uses Django's `UserCreationForm`. `@login_required` guards wishlist views; `LOGIN_URL = '/auth_login/'`.

**Static files:** WhiteNoise (`CompressedManifestStaticFilesStorage`) serves static assets in production. Run `collectstatic` before deploying.

**Templates:** `base1.html` is the base layout (Bootstrap 5 via `django-bootstrap5`). All page templates live flat in `Bookstore1/templates/`.

## URL Structure

| URL | View | Notes |
|-----|------|-------|
| `/` or `/hero/` | `hero` | Landing page |
| `/Allbooks/` | `programming_books_view` | Fetches 40 books from Google Books API |
| `/detail/<book_id>/` | `book_detail` | Single book from Google Books API |
| `/wishlist/` | `wishlist_view` | Login required |
| `/wishlist/add/<book_id>/` | `add_to_wishlist` | POST, login required |
| `/wishlist/remove/<book_id>/` | `remove_from_wishlist` | POST, login required |
| `/auth_login/` | `auth_login` | |
| `/auth_reg/` | `auth_reg` | |
| `/logout/` | `custom_logout` | |
