#!/bin/bash

# Activate virtual environment
source venv/Scripts/activate
pip install -r requirements.txt

# Run the application
cd app
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
