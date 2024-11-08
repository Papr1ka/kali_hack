from typing import Annotated
import aiofiles
from fastapi import APIRouter, Depends, HTTPException, UploadFile, status
from sqlalchemy.ext.asyncio import AsyncSession

from .models import Profile, User

from .schemas import CreateUser, GetProfile, GetUser, UpdateProfile, UpdateUser, GetVideo
from .dependencies import get_file_path, session_dependency, get_profile_by_id
from .service import update_profile
from .models import Video
import os


router = APIRouter(prefix="/compute", tags=["compute"])


@router.post(
    "/video", status_code=status.HTTP_200_OK, response_model=GetVideo
)
async def upload_video(
    video_file: UploadFile,
    profile: Annotated[Profile, Depends(get_profile_by_id)],
    session: Annotated[AsyncSession, Depends(session_dependency)]
):
    video_full_path = get_file_path(profile.id, video_file.filename)
        
    async with aiofiles.open(video_full_path, 'wb') as out_file:
        content = await video_file.read()
        await out_file.write(content)

    await session.refresh(profile, ["video"])

    if profile.video is not None:
        os.remove(profile.video.video_path)
    
    video = Video(owner=profile, video_path=video_full_path)
    session.add(video)
    await session.commit()
    # await session.refresh(profile, ["video"])
    return video
