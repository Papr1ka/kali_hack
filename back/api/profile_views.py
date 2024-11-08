from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from .models import Profile, User

from .schemas import CreateUser, GetProfile, GetUser, UpdateProfile, UpdateUser
from .dependencies import session_dependency, get_profile_by_id
from .service import update_profile


router = APIRouter(prefix="/profiles", tags=["profiles"])


@router.get(
    "/profile/{user_id}", status_code=status.HTTP_200_OK, response_model=GetProfile
)
async def get_user_profile(
    profile: Annotated[Profile, Depends(get_profile_by_id)],
):
    return profile


@router.post("/profile/{user_id}/update", status_code=status.HTTP_200_OK)
async def update_user_view(
    profile: Annotated[Profile, Depends(get_profile_by_id)],
    to_update: UpdateProfile,
    session: AsyncSession = Depends(session_dependency),
):
    return await update_profile(profile, to_update, session)
