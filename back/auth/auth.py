import secrets
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Header, security, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

router = APIRouter(prefix="/auth", tags=["auth"])

security = HTTPBasic()


username_to_password = {"joe": "12345678", "admin": "admin"}

static_auth = {
    "37e95d93e5a97405522a26a7bb07293162f1de482cce7141427beffd5806a0c4": "joe",
    "721a3e73b9ed74b057b63d9548587913c90d7c2a095d0a4903d89de7d80098dd": "admin",
}


def check_user(credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
    unauthorized = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Неверные данные для входа",
        headers={"WWW-Authenticate": "Basic"},
    )
    if credentials.username not in username_to_password:
        raise unauthorized

    if not secrets.compare_digest(
        credentials.password.encode("utf-8"),
        username_to_password[credentials.username].encode("utf-8"),
    ):
        raise unauthorized

    return credentials.username


def get_user_by_token(token: str = Header(alias="x-auth")):
    unauthorized = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Неверный токен",
        headers={"WWW-Authenticate": "Basic"},
    )
    if token not in static_auth:
        raise unauthorized
    return static_auth[token]


@router.get("/login")
async def login(auth_username: str = Depends(check_user)):
    return {"Hello": auth_username}


@router.get("/login_by_header")
def login_by_header(username: str = Depends(get_user_by_token)):
    return {"Hello from headers": username}
