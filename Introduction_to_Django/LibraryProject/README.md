# LibraryProject

## Overview
A basic Django project created inside a Python virtual environment as part of the *Introduction to Django* lab.

## Setup Steps

1. Create and activate a virtual environment:
    python -m venv env
    source env/bin/activate
    ```
2. Install Django:
    pip install django
    ```
3. Start a Django project:
    django-admin startproject LibraryProject
    ```
4. Run the development server:
    python manage.py runserver
    ```
5. Visit the project in your browser:
    [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Project Structure
- **manage.py**: Command-line utility for Django tasks.
- **settings.py**: Project configuration.
- **urls.py**: URL routing definitions.
- **asgi.py / wsgi.py**: Server gateways for deployment.
