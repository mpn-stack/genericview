#!/bin/bash

SUPERUSER=${DJANGO_SUPERUSER:-"admin"}
SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL:-"admin@bookstore.com"}

/opt/venv/bin/python manage.py migrate --noinput
/opt/venv/bin/python manage.py createsuperuser --username $SUPERUSER --email $SUPERUSER_EMAIL --noinput || true
