#!/usr/bin/env sh

MODE=${MODE:-"run"}

case "$MODE" in
    "run")
        echo "Running Django server"
        python manage.py runserver
        ;;
    "migrate")
        echo "Running Django migrations"
        python manage.py migrate
        ;;
    *)
        echo "Unknown mode: $MODE"
        exit 1
        ;;
esac
