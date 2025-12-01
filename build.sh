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

# --- AUTOMATED SUPERUSER CREATION ---
echo "--- Checking for and creating superuser ---"
# This runs Python code inside the Django environment
python manage.py shell <<EOF
from django.contrib.auth import get_user_model
import os

User = get_user_model()
username = os.environ.get('DJANGO_SUPERUSER_USERNAME')
password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')

# Only create the user if the variables are set AND the user doesn't exist
if username and password and not User.objects.filter(username=username).exists():
    # Use a dummy email since Django requires one for createsuperuser
    User.objects.create_superuser(username=username, password=password, email='admin@lumitech.com')
    print("Automated superuser created successfully!")
else:
    print("Superuser already exists or environment variables were missing during build.")
EOF