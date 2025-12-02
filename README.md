# Receipe_Project

This is a Django web application for managing recipe entries (images, names, descriptions) with user authentication.

**Repository Root**: `d:/django/core1`

**Apps included**:
- `Accounts` : custom user-related code
- `home` : public pages (home, about, contact)
- `vege` : recipe management (create, update, delete, list)

Database: SQLite (`db.sqlite3`)

Prerequisites
- Python 3.9+ (or the version you use for the project)
- Django installed in your environment

Quick setup
- Create and activate a virtual environment:
```
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```
- Install dependencies (if you maintain a `requirements.txt` add it and run `pip install -r requirements.txt`). At minimum, install Django:
```
pip install Django
```
- Apply migrations and run the server:
```
python manage.py migrate
python manage.py runserver
```

Media and static files
- Media is served via `settings.MEDIA_URL` when `DEBUG` is `True`. Uploaded recipe images are stored under `media/receipe/`.
- Static files are served in development via `staticfiles_urlpatterns()`.

Models (summary)
- `vege.models.Receipe`:
  - `user` (ForeignKey to Django `User`, nullable)
  - `receipe_name` (CharField)
  - `receipe_description` (TextField)
  - `receipe_image` (ImageField, upload_to=`receipe`)
  - `receipe_view_count` (IntegerField, default=1)

Endpoints
The project's URL configuration is in `core1/urls.py`. Below are the main endpoints, HTTP methods, and notes about authentication and behaviour.

- **`/`**: GET — Home page. Renders `home/index.html` and passes `peoples` and `vegetables` in context. (View: `home.views.home`)

- **`/receipes/`**: GET, POST — List recipes (GET) and create a new recipe (POST).
  - GET: returns `receipes.html` with context `{'receipes': queryset}`. Supports query `?search=...` to filter by recipe name.
  - POST: authenticated users can upload a recipe image and provide `receipe_name` and `receipe_description`. Creates `Receipe` and redirects to `/receipes/`.
  - Authentication: login required (decorated with `@login_required(login_url="/login/")`). (View: `vege.views.receipes`)

- **`/delete-receipe/<id>/`**: GET — Delete a recipe by `id` and redirect to `/receipes/`.
  - Note: This view (`vege.views.delete_receipe`) does not have an authentication decorator in the current codebase, so calling this URL will delete the item for any request; consider protecting it with login/permission checks.

- **`/update-receipe/<id>/`**: GET, POST — Update an existing recipe.
  - GET: Renders `update_receipes.html` with the recipe in context.
  - POST: Updates `receipe_name`, `receipe_description` and optionally `receipe_image`; then redirects to `/receipes/`.
  - Authentication: login required (`@login_required(login_url="/login/")`). (View: `vege.views.update_receipe`)

- **`/login/`**: GET, POST — Login page (`vege.views.login_page`).
  - GET: renders `login.html`.
  - POST: expects `username` and `password`, authenticates with Django auth; on success redirects to `/receipes/`, otherwise shows messages and redirects back to `/login/`.

- **`/register/`**: GET, POST — Register a new user (`vege.views.register`).
  - POST fields: `first_name`, `last_name`, `username`, `password`.
  - Creates a Django `User` and stores hashed password via `set_password`.

- **`/logout/`**: GET — Logs out the current user and redirects to `/login/`.

- **`/about/`**: GET — Renders `home/about.html` (View: `home.views.about`).

- **`/contact/`**: GET — Renders `home/contact.html` (View: `home.views.contact`).

- **`/success-page/`**: GET — Returns a simple HttpResponse for success (View: `home.views.success_page`).

- **`/admin/`**: Django admin site.

Notes & recommendations
- Protect destructive actions: `delete_receipe` currently allows deletion without authentication — consider adding `@login_required` and permission checks.
- Add a `requirements.txt` with pinned dependencies to make setup reproducible.
- For production, configure proper media/static hosting (e.g., cloud storage or a static server) and disable Django's debug media serving.

If you want, I can:
- run the development server and show the endpoints live,
- add `@login_required` to `delete_receipe` and create a minimal `requirements.txt`, or
- generate API-style documentation (OpenAPI) for these views.

---
Generated on: 2025-12-02
