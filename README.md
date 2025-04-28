# Fastapi Boilerplate project

This is a boilerplate project for fastapi. It is based on the [fastapi official tutorial](https://fastapi.tiangolo.com/tutorial/first-steps/). It aims to be a simple MVC project with a database connection. The example is a simple todo list.

It uses [Jinja2](https://jinja.palletsprojects.com/en/3.0.x/) as a template engine and [Prisma](https://prisma-client-py.readthedocs.io/en/stable/) as an ORM.

For the frontend, it uses [Bootstrap](https://getbootstrap.com/) and [HTMX](https://htmx.org/).

## Requirements

- [Docker](https://docs.docker.com/get-docker/) and [docker-compose](https://docs.docker.com/compose/) v2 for running the project
- [Python 3.12+](https://www.python.org/) and [uv](https://docs.astral.sh/uv/) for development

## Quickstart

### Running the project

```bash
cp docker-compose.override.yml.dist docker-compose.override.yml 
docker compose up

# Service is running on http://localhost:8000
```

### Development


To improve development experience, a devcontainer configuration is available. To setup a development environment, you can simply use [Vscode Devcontainer](https://youtu.be/b1RavPr_878). Once the devcontainer is up, just run the command `uv run fastapi dev ./app/main.py` to start the dev server that will be available on [localhost:8000](http://localhost:8000)

Else, you can follow those steps to configure the development environment on your host:


```bash
# Install dependencies
uv sync --all-groups --frozen

# Install prisma client
uv run prisma migrate dev --schema database/schema.prisma

# Run the project
uv run fastapi dev ./app/main.py
```

### Project quality

```bash
# Run linters
uv run ruff check . --fix
```

## Application structure

### Declare a new route

To declare a new route, you need to create a new file in the `app/routes` directory. The file must contain a `router` variable that is an instance of `fastapi.APIRouter`. It will be automaticaly binded to the fastapi application.

```python
# app/routes/my_route.py
from fastapi import APIRouter

router = APIRouter(prefix="/my_route")

@router.get("/helloworld")
async def my_route():
    return {"message": "Hello World"}
```
