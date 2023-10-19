from typing import Annotated

from fastapi import APIRouter, Form
from fastapi.requests import Request
from fastapi.responses import HTMLResponse

from config.template import templates
from database.engine import db

router = APIRouter(prefix="/tasks")


@router.get("/", tags=["tasks"], response_class=HTMLResponse, name="get_all_tasks")
async def homepage(request: Request):
    return templates.TemplateResponse(
        name="tasks/home.html",
        context={
            "request": request,
            "title": "Todo List",
            "tasks": await db.task.find_many(),
        },
    )


@router.delete(
    path="/{task_id}", tags=["tasks"], response_class=HTMLResponse, name="delete_task"
)
async def delete_task(task_id: int):
    await db.task.delete({"id": task_id})

    return HTMLResponse("")


@router.put(
    "/{task_id}", tags=["tasks"], response_class=HTMLResponse, name="update_task"
)
async def update_task(
    request: Request,
    task_id: int,
    name: Annotated[str, Form()],
    description: Annotated[str, Form()],
):
    return templates.TemplateResponse(
        name="tasks/partials/task-row.html",
        context={
            "request": request,
            "task": await db.task.update(
                where={"id": task_id}, data={"name": name, "description": description}
            ),
        },
    )


@router.put(
    "/{task_id}/toggle_status",
    tags=["tasks"],
    response_class=HTMLResponse,
    name="toggle_task_status",
)
async def toggle_task_status(task_id: int, request: Request):
    task = await db.task.find_unique(where={"id": task_id})
    updated_task = await db.task.update(
        where={"id": task_id}, data={"status": not task.status}
    )

    return templates.TemplateResponse(
        name="tasks/partials/task-row.html",
        context={
            "request": request,
            "task": updated_task,
        },
    )


@router.post("/", tags=["tasks"], response_class=HTMLResponse, name="add_task")
async def add_task(
    request: Request, name: Annotated[str, Form()], description: Annotated[str, Form()]
):
    return templates.TemplateResponse(
        name="tasks/partials/task-row.html",
        context={
            "request": request,
            "task": await db.task.create({"name": name, "description": description}),
        },
    )


@router.get(
    "/{task_id}", tags=["tasks"], response_class=HTMLResponse, name="get_task_form"
)
async def get_task_form(request: Request, task_id: int):
    return templates.TemplateResponse(
        name="tasks/partials/task-form.html",
        context={
            "request": request,
            "task": await db.task.find_unique(where={"id": task_id}),
        },
    )
