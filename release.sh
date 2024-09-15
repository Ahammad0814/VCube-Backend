#!/usr/bin/env sh

# Run database migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Start the Gunicorn server
exec gunicorn VCube_Data_API.wsgi:application --bind 0.0.0.0:8000
