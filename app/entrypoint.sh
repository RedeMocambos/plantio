#!/usr/bin/env bash

python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --no-input

gunicorn plantio.wsgi -b :8000
