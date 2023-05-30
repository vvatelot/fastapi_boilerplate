import asyncio

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from config.env import DEBUG
from config.routes import router
from database.engine import db

app = FastAPI(debug=DEBUG)

app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(router)


@app.on_event(event_type="startup")
def on_startup():
    db.init()
    asyncio.create_task(db.create_all())
