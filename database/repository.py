from typing import List, Literal

from pydantic import BaseModel
from sqlalchemy import delete as sqlalchemy_delete
from sqlalchemy import update as sqlalchemy_update
from sqlalchemy.sql.expression import asc, desc
from sqlmodel import select

from database.engine import db


class Sort(BaseModel):
    clause: str
    sort: Literal["asc", "desc"]


class BaseRepository:
    @classmethod
    async def get_all(
        cls,
        limit: int | None = None,
        offset: int | None = None,
        where: List = [],
        sort_params: List[Sort] = [],
        **kwargs
    ):
        query = select(cls)
        print("where: ", where)
        if limit:
            query = query.limit(limit)
        if offset:
            query = query.offset(offset)
        for w in where:
            query = query.where(w)

        for sort in sort_params:
            if sort.sort == "asc":
                sort_parameter = asc(sort.clause)
            elif sort.sort == "desc":
                sort_parameter = desc(sort.clause)

            query = query.order_by(sort_parameter)

        return (await db.execute(query)).scalars().all()

    @classmethod
    async def get(cls, id):
        query = select(cls).where(cls.id == id)
        return (await db.execute(query)).scalar_one_or_none()

    @classmethod
    async def create(cls, name: str, description: str, **kwargs):
        task = cls(name=name, description=description, **kwargs)
        db.add(task)
        try:
            await db.commit()
        except Exception:
            await db.rollback()
            raise
        return task

    @classmethod
    async def update(cls, id, **kwargs):
        query = (
            sqlalchemy_update(cls)
            .where(cls.id == id)
            .values(**kwargs)
            .execution_options(synchronize_session="fetch")
        )
        await db.execute(query)

        try:
            await db.commit()
        except Exception:
            await db.rollback()
            raise

    @classmethod
    async def delete(cls, id):
        query = sqlalchemy_delete(cls).where(cls.id == id)
        await db.execute(query)
        try:
            await db.commit()
        except Exception:
            await db.rollback()
            raise

        return True
        return True

    @classmethod
    async def find_by(cls, **kwargs):
        query = select(cls).where(**kwargs)
        return (await db.execute(query)).scalars().all()

    def __config__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
            setattr(self, key, value)
            setattr(self, key, value)
            setattr(self, key, value)
