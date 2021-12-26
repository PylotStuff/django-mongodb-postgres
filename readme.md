# MongoDB and Postgres integration with Django

This project includes multiple database configurations to launch Django project with **Postgres** and **MongoDB**.

## Getting Started

This project works on **Python 3+** and **Django 3.1.3**. If you want to change the Django version please follow the link below to get information about it.

[Add MongoDB and PostgreSQL in Django using Docker](https://thepylot.dev)

Run the following command to makemigrations:

```
docker-compose run app sh -c "python manage.py makemigrations core"
```

then start the containers:

```
docker-compose up -d
```

After containers launched navigate to `/` home path and `celery` will automatically receive the task.
