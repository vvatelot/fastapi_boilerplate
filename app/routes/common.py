from fastapi import APIRouter
from fastapi.requests import Request
from fastapi.responses import HTMLResponse

from config.template import templates

router = APIRouter(tags=["common"])


@router.get("/", response_class=HTMLResponse)
async def homepage(request: Request):
    return templates.TemplateResponse(
        name="homepage.html",
        context={
            "request": request,
        },
    )
