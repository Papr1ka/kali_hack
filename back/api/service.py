from .models import User, Profile
from .schemas import CreateUser, UpdateProfile, UpdateUser
from .models import User, Profile
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select


# Тут везде, где _user, для пользователя будет недоступен profile!
# Будет misset_greenlet, чтобы был доступен, надо session.refresh(user, ['profile'])


async def register_user(user_to_create: CreateUser, session: AsyncSession) -> User:
    """
    Когда пользователь регистрируется
    """
    user = User(**user_to_create.model_dump())
    profile = Profile(user=user)
    session.add(profile)

    await session.commit()
    return user


async def get_user(user_id: int, session: AsyncSession) -> User:
    return await session.get(User, user_id)
    # if user is not None:
    #     await session.refresh(user, ["profile"])
    return user


async def delete_user(user: User, session: AsyncSession):
    await session.delete(user)
    await session.commit()


async def update_user(user: User, to_update: UpdateUser, session: AsyncSession):
    for name, value in to_update.model_dump().items():
        setattr(user, name, value)
    session.add(user)
    await session.commit()
    return user


async def update_profile(
    profile: Profile, to_update: UpdateProfile, session: AsyncSession
):
    for name, value in to_update.model_dump().items():
        setattr(profile, name, value)
    session.add(profile)
    await session.commit()
    return profile
