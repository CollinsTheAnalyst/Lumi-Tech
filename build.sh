# File: build.sh

#!/usr/bin/env bash
# Exit on error
set -o errexit

echo "--- Installing dependencies ---"
pip install -r requirements.txt 

echo "--- Collecting static files ---"
# Collects CSS, JS, etc., into the 'staticfiles' directory
python manage.py collectstatic --no-input

echo "--- Running database migrations ---"
# Creates the necessary tables in the new PostgreSQL database
python manage.py migrate

echo "--- Loading initial data fixture ---"
# VITAL: Imports data from the initial_data.json file into the new database
python manage.py loaddata initial_data.json

# You can add a command here to create a superuser if you want
# python manage.py createsuperuser --no-input