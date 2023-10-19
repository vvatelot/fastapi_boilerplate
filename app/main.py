from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.routes import router
from config.env import DEBUG
from database.engine import prisma


def init_app():
    app = FastAPI(debug=DEBUG)

    app.mount("/static", StaticFiles(directory="static"), name="static")
    app.include_router(router)

    @app.on_event(event_type="startup")
    async def on_startup():
        await prisma.connect()

    @app.on_event(event_type="shutdown")
    async def on_shutdown():
        await prisma.disconnect()

    return app


app = init_app()
