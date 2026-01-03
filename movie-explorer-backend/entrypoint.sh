#!/bin/bash

# Check if arguments are passed (for custom commands like makemigrations)
if [ $# -gt 0 ]; then
    # Execute the passed command directly
    exec "$@"
else
    # Default startup: migrate and run server
    python manage.py migrate
    python manage.py runserver 0.0.0.0:8000
fi
