from typing import Annotated, AsyncGenerator, Coroutine
from fastapi import Depends, HTTPException, Path, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import SQLModel

from .models import Profile, User

from .service import get_user
from .db import session_factory
from ..config import settings
import os


async def session_dependency() -> AsyncGenerator[AsyncSession, None]:
    async with session_factory() as session:
        yield session
        await session.close()


# def generate_get_object_by_id(db_model: SQLModel, alias="object_id"):
#     async def get_object_by_id(
#         session: Annotated[AsyncSession, Depends(session_dependency)],
#         object_id: int = Path(alias=alias),
#     ):
#         obj = await session.get(db_model, object_id)
#         if obj is None:
#             raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Объект не найден")
#         return obj

#     return get_object_by_id


# get_user_by_id: Coroutine = generate_get_object_by_id(User, "user_id")
# get_profile_by_id: Coroutine = generate_get_object_by_id(Profile, "user_id")

async def get_user_by_id(
    session: Annotated[AsyncSession, Depends(session_dependency)],
    user_id: int,
):
    obj = await session.get(User, user_id)
    if obj is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Объект не найден")
    return obj

async def get_profile_by_id(
    session: Annotated[AsyncSession, Depends(session_dependency)],
    user_id: int,
):
    obj = await session.get(Profile, user_id)
    if obj is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Объект не найден")
    return obj

def get_file_path(user_id: int, filename: str):
    return os.path.join(settings.static_dir_path, f"{user_id}_{filename}")
