from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from .models import User

from .schemas import CreateUser, GetUser, UpdateUser
from .dependencies import session_dependency, get_user_by_id
from .service import delete_user, register_user, update_user


router = APIRouter(prefix="/users", tags=["users"])


@router.post("/register", response_model=GetUser, status_code=status.HTTP_201_CREATED)
async def register_user_view(
    new_user: CreateUser, session: Annotated[AsyncSession, Depends(session_dependency)]
):
    user = await register_user(new_user, session)
    return user


@router.post("/user/{user_id}/delete", status_code=status.HTTP_200_OK)
async def delete_user_view(
    user: Annotated[
        User,
        Depends(get_user_by_id),
    ],
    session: AsyncSession = Depends(session_dependency),
):
    await delete_user(user, session)


@router.post("/user/{user_id}/update", status_code=status.HTTP_200_OK)
async def update_user_view(
    user: Annotated[User, Depends(get_user_by_id)],
    to_update: UpdateUser,
    session: AsyncSession = Depends(session_dependency),
):
    return await update_user(user, to_update, session)


@router.get("/user/{user_id}", response_model=GetUser, status_code=status.HTTP_200_OK)
async def get_user_view(
    user: Annotated[User, Depends(get_user_by_id)],
):
    return user
