#!/bin/sh

alembic upgrade head
gunicorn app.main:app --timeout 0 --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000 --forwarded-allow-ips="*"