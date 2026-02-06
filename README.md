# CodeStar Blog

A full-featured Django blog platform with user authentication, comment management, and cloud-based image hosting.

## Overview

CodeStar Blog is a modern, responsive blogging platform built with Django that enables users to create, publish, and manage blog posts. It features a clean interface, user authentication, real-time comment moderation, and secure content management.

## Features

- **Blog Post Management**: Create, edit, and publish blog posts with rich text editing (Summernote)
- **User Authentication**: Secure user registration and login via Django Allauth
- **Featured Images**: Upload and manage featured images for posts with Cloudinary integration
- **Comment System**: Readers can comment on posts with admin moderation
- **Post Filtering**: Display filtered published posts on the homepage with pagination
- **User Profiles**: User profile pages with profile image support
- **Collaboration Requests**: Features for collaboration requests between users
- **Responsive Design**: Bootstrap 5 styling for mobile-friendly experience

## Tech Stack

- **Backend**: Django 4.2
- **Database**: PostgreSQL
- **Image Storage**: Cloudinary
- **Frontend**: Bootstrap 5, HTML5, CSS3
- **Rich Text Editor**: Summernote
- **Authentication**: Django Allauth
- **Deployment**: Gunicorn, Heroku (Procfile included)
- **Package Management**: pip

### Key Dependencies

- django-crispy-forms (Form styling)
- django-summernote (Rich text editing)
- cloudinary (Image hosting)
- dj3-cloudinary-storage (Django Cloudinary integration)
- django-allauth (User authentication)
- psycopg2 (PostgreSQL adapter)

## Installation

### Prerequisites

- Python 3.8+
- PostgreSQL
- Cloudinary account

### Steps

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd codestar_blog
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Configuration**
   Create an `env.py` file in the project root and add:

   ```python
   import os

   os.environ['SECRET_KEY'] = 'your-secret-key'
   os.environ['DEBUG'] = 'True'
   os.environ['ALLOWED_HOSTS'] = 'localhost,127.0.0.1'
   os.environ['DATABASE_URL'] = 'your-database-url'
   os.environ['CLOUDINARY_URL'] = 'your-cloudinary-url'
   ```

5. **Run migrations**

   ```bash
   python manage.py migrate
   ```

6. **Create a superuser**

   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**

   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   - Blog: http://localhost:8000/
   - Admin: http://localhost:8000/admin/

## Project Structure

```
codestar_blog/
├── blog/                 # Main blog app (posts, comments)
├── about/                # About/profile app
├── codestar/             # Project settings and configuration
├── templates/            # HTML templates
├── static/               # CSS, JavaScript files
├── db.sqlite3            # Development database
├── manage.py             # Django management script
├── requirements.txt      # Python dependencies
└── README.md             # This file
```

## Usage

### Creating a Blog Post

1. Login to the admin panel at `/admin/`
2. Navigate to **Posts** section
3. Click **Add Post** and fill in:
   - Title
   - Content (using Summernote editor)
   - Featured Image
   - Excerpt (optional)
   - Status (Draft/Published)
4. Click **Save**

### Managing Comments

1. Go to the admin panel
2. Select **Comments** to view and approve user comments
3. Approved comments appear on published posts

## Models

### Post

- Title, Slug, Author, Content
- Featured Image, Excerpt
- Created/Updated timestamps
- Publication Status
- Related Comments

### Comment

- Post (Foreign Key)
- Author (User)
- Body text
- Created timestamp
- Approval status

### Collaboration Request

- Tracks collaboration requests between users

## Testing

Run tests with:

```bash
python manage.py test
```

Test files are included:

- `blog/tests.py` - Blog app tests
- `blog/test_forms.py` - Form validation tests
- `blog/tests_views.py` - View tests
- `about/tests.py` - About app tests

## Deployment

The project includes a `Procfile` for Heroku deployment. Set required environment variables on your hosting platform before deploying.

## License

This project is part of the Code Institute curriculum.
