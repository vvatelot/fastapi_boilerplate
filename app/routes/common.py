from fastapi import APIRouter
from fastapi.requests import Request
from fastapi.responses import HTMLResponse

from app.routes.tasks import homepage as task_homepage

router = APIRouter(tags=["common"])


@router.get("/", response_class=HTMLResponse)
async def homepage(request: Request):
    return await task_homepage(request=request)
