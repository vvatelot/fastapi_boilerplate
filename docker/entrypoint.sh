#!/bin/sh

uv run prisma migrate dev --schema database/schema.prisma
uv run fastapi run ./app/main.py