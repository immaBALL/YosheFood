#!/bin/bash
# Build script for Railway deployment

# Collect static files
python manage.py collectstatic --noinput

# Run migrations
python manage.py migrate 