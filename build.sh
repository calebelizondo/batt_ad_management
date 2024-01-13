#!/bin/bash

# Activate virtual environment
source .env

source venv/Scripts/activate
pip install -r requirements.txt
python manage.py createsuperuser --noinput \
    --username="$SUPERUSER_USERNAME" \
    --email="$SUPERUSER_EMAIL" \
    --password="$SUPERUSER_PASSWORD"

cd ..