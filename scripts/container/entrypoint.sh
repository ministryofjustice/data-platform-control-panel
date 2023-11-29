#!/usr/bin/env sh

MODE=${MODE:-"run"}

case "$MODE" in
"run")
  echo "Running Django server"
  gunicorn -b 0.0.0.0:8000 -k uvicorn.workers.UvicornWorker -w 4 controlpanel.asgi:application
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
