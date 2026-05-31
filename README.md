# Photography & Videography Blog

A Django-based blog website for a photography, advertising, and videography business.

## Features
- Home page with placeholder blog/portfolio cards
- User registration and login
- Profile page for authenticated users
- MySQL database configured for `bank`

## Setup
1. Install dependencies:

```powershell
python -m pip install -r requirements.txt
```

2. Create the MySQL database named `bank`.
3. Confirm MySQL is running on `localhost:3306`.
4. Run migrations:

```powershell
python manage.py migrate
```

5. Create a superuser if desired:

```powershell
python manage.py createsuperuser
```

6. Use the Django admin interface to add, edit, and delete blog posts:

- Go to `http://127.0.0.1:8000/admin/`
- Log in with the superuser credentials
- Manage `Posts` through the admin UI

7. Start the development server:

```powershell
python manage.py runserver
```

## Database configuration
The project is already configured to use MySQL with:
- NAME: `blog_post`
- USER: `root`
- PASSWORD: `7303025805pps`
- HOST: `127.0.0.1`
- PORT: `3306`

If you need to change the database credentials, update `blogsite/settings.py`.
