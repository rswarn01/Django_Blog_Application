# Django_Blog_Application

This is a simple blog application built with Django and Django REST Framework, featuring basic CRUD functionalities, user authentication, and Swagger documentation.

## Features

- User registration and authentication
- Create, read, update, and delete blog posts
- Create and read comments for blog posts
- Pagination for list of posts
- Token-based authentication
- Swagger documentation for APIs

## Setup Instructions

### Prerequisites
Ensure you have the following installed on your system:

- Python 3.8+
- pip (Python package installer)
- virtualenv (optional but recommended)

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/django-blog-application.git
    cd django-blog-application
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv blogenv
    source blogenv/bin/activate  # On Windows use `blogenv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply database migrations:**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Create a superuser for the admin panel:**

    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

### Configuration

#### Settings

Adjust any necessary settings in `blog_project/settings.py`. Important settings include:

- `DEBUG`: Set to `True` for development, `False` for production.
- `ALLOWED_HOSTS`: Add your domain or IP address.
- `DATABASES`: Configure your database settings.

#### Swagger Documentation

Swagger and ReDoc documentation can be accessed at the following URLs:

- Swagger: `http://127.0.0.1:8000/swagger/`
- ReDoc: `http://127.0.0.1:8000/redoc/`

### API Endpoints

- **User Registration:**
  - `POST /api/register/`
- **Token Authentication:**
  - `POST /api/token/` (obtain token)
  - `POST /api/token/refresh/` (refresh token)
- **Posts:**
  - `GET /api/posts/` (list posts, paginated)
  - `POST /api/posts/` (create post)
  - `GET /api/posts/<id>/` (retrieve post)
  - `PUT /api/posts/<id>/` (update post)
  - `DELETE /api/posts/<id>/` (delete post)
- **Comments:**
  - `GET /api/posts/<post_id>/comments/` (list comments for a post)
  - `POST /api/posts/<post_id>/comments/` (create comment for a post)

### Running Tests

To run the tests, use the following command (not working correctly):

```bash
python manage.py test
