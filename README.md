UAV Rental Platform 

Overview

This documentation provides information about the setup and management of the UAV Rental Platform Django project.
Environment

    Python version: Python 3.11.9
    Django version: django 5.0.6
    Database: PostgreSQL16, pgAdmin4


Getting Started

To get started with the project, follow these steps:

    Clone the repository:
    git clone https://github.com/halitekmekcioglu/uavr

    bash


Install dependencies:

    pip install -r requirements.txt

Apply database migrations:
    
    python manage.py migrate

Create a superuser for the admin interface:

    python manage.py createsuperuser

Start the development server:

    python manage.py runserver

Database Information

The project uses uav_rental_db for data storage.

    Database name: uav_rental_db
    Host: localhost
    Port: 5432
    Username: postgres
    Password: 123
    ENGINE': django.db.backends.postgresql
    

Administration

To access the Django admin interface, follow these steps:

    Start the development server if not already running:

    python manage.py runserver

 Open a web browser and go to the admin URL: http://127.0.0.1:8000/admin
 Enter the username and password of the superuser created earlier.

Project Structure

        uav_rental: main app folder.
        models.py: uav models.
        views.py: Views for handling HTTP requests.
        urls.py: URL patterns for routing requests to views.
        admin.py: Admin configurations.
        forms.py: Forms for user input validation.
        templates/: HTML templates.
        static/: Static files (CSS, JavaScript, images).
        migrations/: Database migrations.
