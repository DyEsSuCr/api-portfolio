#!/usr/bin/env bash
# exit on error
set -o errexit

export DJANGO_SUPERUSER_USERNAME=
export DJANGO_SUPERUSER_PASSWORD=
export DJANGO_SUPERUSER_EMAIL=

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate

python manage.py createsuperuser --no-input