#!/bin/bash
cd app
python manage.py makemigrations
python manage.py migrate
gunicorn app.wsgi:application --workers 4