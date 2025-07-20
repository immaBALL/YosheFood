#!/bin/bash
# Start script for Railway deployment

# Activate virtual environment
. /opt/venv/bin/activate

# Run migrations
python manage.py migrate

# Start gunicorn
exec gunicorn myproject.wsgi:application --bind 0.0.0.0:$PORT --workers 2 --timeout 120 