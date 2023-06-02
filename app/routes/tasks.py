from typing import Annotated

from fastapi import APIRouter, Form
from fastapi.requests import Request
from fastapi.responses import HTMLResponse

from app.models.tasks import Task
from config.template import templates

router = APIRouter(prefix="/tasks")


@router.get("/", tags=["tasks"], response_class=HTMLResponse, name="get_all_tasks")
async def homepage(request: Request):
    return templates.TemplateResponse(
        name="tasks/home.html",
        context={
            "request": request,
            "title": "Todo List",
            "tasks": await Task.get_all(),
        },
    )


@router.delete(
    path="/{task_id}", tags=["tasks"], response_class=HTMLResponse, name="delete_task"
)
async def delete_task(task_id: int):
    await Task.delete(task_id)

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
    await Task.update(task_id, name=name, description=description)

    return templates.TemplateResponse(
        name="tasks/partials/task-row.html",
        context={
            "request": request,
            "task": Task(id=task_id, name=name, description=description),
        },
    )


@router.put(
    "/{task_id}/toggle_status",
    tags=["tasks"],
    response_class=HTMLResponse,
    name="toggle_task_status",
)
async def toggle_task_status(task_id: int):
    await Task.toggle_status(task_id)

    return HTMLResponse("")


@router.post("/", tags=["tasks"], response_class=HTMLResponse, name="add_task")
async def add_task(
    request: Request, name: Annotated[str, Form()], description: Annotated[str, Form()]
):
    task = await Task.create(name, description)

    return templates.TemplateResponse(
        name="tasks/partials/task-row.html",
        context={
            "request": request,
            "task": task,
        },
    )


@router.get(
    "/{task_id}", tags=["tasks"], response_class=HTMLResponse, name="get_task_form"
)
async def get_task_form(request: Request, task_id: int):
    task = await Task.get(task_id)

    return templates.TemplateResponse(
        name="tasks/partials/task-form.html",
        context={
            "request": request,
            "task": task,
        },
    )
