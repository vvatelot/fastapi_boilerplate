from sqlmodel import Field, SQLModel

from database.repository import BaseRepository


class Task(BaseRepository, SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str | None
    status: bool = False
    description: str | None = None

    @classmethod
    async def toggle_status(cls, task_id: int, **kwargs) -> None:
        task = await Task.get(task_id)
        task.status = not task.status
        await task.update(task_id, status=task.status)
