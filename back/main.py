from contextlib import asynccontextmanager
from .config import settings
from fastapi import FastAPI
from .auth.auth import router as auth_router
from .api.user_views import router as users_router
from .api.profile_views import router as profiles_router
from .api.model_views import router as compute_router


from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory=settings.static_dir_path), name="static")


app.include_router(auth_router)
app.include_router(users_router)
app.include_router(profiles_router)
app.include_router(compute_router)


@app.get("/")
def hello():
    return {"hello": "world"}
