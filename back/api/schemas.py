from typing import Optional
from pydantic import BaseModel


class CreateUser(BaseModel):
    username: str
    password: str


class GetUser(BaseModel):
    id: int
    username: str
    # profile: "OutProfile"


class UpdateUser(BaseModel):
    username: Optional[str]
    password: Optional[str]


class UpdateProfile(BaseModel):
    name: Optional[str] = None
    surname: Optional[str] = None
    patronymic: Optional[str] = None
    phone_number: Optional[str] = None


class GetProfile(BaseModel):
    id: int
    name: Optional[str]
    surname: Optional[str]
    patronymic: Optional[str]
    phone_number: Optional[str]


class InVacancy(BaseModel):
    name: str
    description: str

class GetVideo(BaseModel):
    """
    Класс для хранения видео-визиток
    """
    id: int
    owner_id: int
    # Путь к видео-визитке (mp4 файл)
    video_path: str
