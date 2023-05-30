from sqlmodel import Field, SQLModel

from database.repository import BaseRepository


class Task(BaseRepository, SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str | None
    status: bool = False
    description: str | None = None
