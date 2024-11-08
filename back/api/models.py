from typing import List, Optional
from sqlmodel import SQLModel
from sqlmodel import Field, Relationship


class User(SQLModel, table=True):
    """
    Базовый класс пользователя, в том числе для авторизации
    """

    __tablename__ = "users"

    id: int | None = Field(default=None, primary_key=True, index=True, nullable=False)
    username: str = Field(index=True)
    password: str
    profile: "Profile" = Relationship(
        sa_relationship_kwargs={"uselist": False},
        back_populates="user",
        cascade_delete=True,
    )


class ProfileVacancyLink(SQLModel, table=True):
    """
    Таблица Many-To-Many, для Profile и Vacancy
    Один пользователь может иметь несколько (топ 10) vacancies, которые для него наиболее хорошо подходят
    Одна вакансия может иметь несколько (топ 10) пользователей, которые для неё подходят
    """

    __tablename__ = "profile_vacancy"

    profile_id: Optional[int] = Field(
        default=None, foreign_key="profiles.id", primary_key=True, ondelete="CASCADE"
    )
    vacancy_id: Optional[int] = Field(
        default=None, foreign_key="vacancies.id", primary_key=True, ondelete="CASCADE"
    )
    probability: int

    profile: "Profile" = Relationship(back_populates="top_vacancies")
    vacancy: "Vacancy" = Relationship(back_populates="top_users")


class Profile(SQLModel, table=True):
    """
    Класс со всей инфой пользователя
    One-To-One к User
    """

    __tablename__ = "profiles"

    id: int | None = Field(default=None, primary_key=True, index=True, nullable=False)

    # one-to-one реализация
    user: User = Relationship(
        sa_relationship_kwargs={"uselist": False},
        back_populates="profile",
    )
    user_id: int = Field(default=None, foreign_key="users.id", ondelete="CASCADE")

    name: Optional[str]
    surname: Optional[str]
    patronymic: Optional[str]
    phone_number: Optional[str]

    # Вакансии, которые оставил сам пользователь как работодатель, one-to-many
    vacancies: List["Vacancy"] = Relationship(
        back_populates="owner", cascade_delete=True
    )

    # Вакансии, которые подходят пользователю как соискателю, one-to-many
    top_vacancies: List["ProfileVacancyLink"] = Relationship(
        back_populates="profile", cascade_delete=True
    )

    # Последняя видеовизитка, которую он загрузил, one-to-one
    video: Optional["Video"] = Relationship(
        cascade_delete=True,
        sa_relationship_kwargs={"uselist": False},
        back_populates="owner",
    )


class Video(SQLModel, table=True):
    """
    Класс для хранения видео-визиток
    """

    __tablename__ = "videos"

    id: int | None = Field(default=None, primary_key=True, index=True, nullable=False)

    # one-to-one
    owner: "Profile" = Relationship(back_populates="video")
    owner_id: int = Field(default=None, foreign_key="profiles.id", ondelete="CASCADE")

    # Путь к видео-визитке (mp4 файл)
    video_path: str

    # Связь с результатом обработки видео моделями
    result: Optional["ModelResult"] = Relationship(
        back_populates="video",
        cascade_delete=True,
        sa_relationship_kwargs={"uselist": False},
    )


class ModelResult(SQLModel, table=True):
    __tablename__ = "model_results"

    id: int | None = Field(default=None, primary_key=True, index=True, nullable=False)

    # Видео, которое было обработано, one-to-one
    video: Video = Relationship(back_populates="result")
    video_id: int = Field(default=None, foreign_key="videos.id", ondelete="CASCADE")
    # Что-то полезное от модели, можно расширять поля
    summary: str


class Vacancy(SQLModel, table=True):
    """
    Таблица вакансий
    """

    __tablename__ = "vacancies"

    id: int | None = Field(default=None, primary_key=True, index=True, nullable=False)

    # Кто создал вакансию - FK к Profile
    owner: Profile = Relationship(back_populates="vacancies")
    owner_id: int = Field(default=None, foreign_key="profiles.id", ondelete="CASCADE")
    name: str
    description: str

    # Топ подходящих к вакансии пользователей
    top_users: List["ProfileVacancyLink"] = Relationship(back_populates="vacancy")
