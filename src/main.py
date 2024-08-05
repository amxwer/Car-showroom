import os
from contextlib import asynccontextmanager
from collections.abc import AsyncIterator
from pathlib import Path

from redis import asyncio as aioredis, StrictRedis
from fastapi import FastAPI, Depends

from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from starlette.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles

from auth.base_config import current_user, fastapi_users, auth_backend
from auth.models import User
from auth.schemas import UserRead, UserCreate
from cars.router import router as router_car
from tasks.router import router as router_tasks
from pages.router import router as router_pages
app = FastAPI(
    title = "app",
    debug=True
)

root_directory = Path(__file__).resolve().parent.parent
static_directory = root_directory / "static"

# Монтируем статические файлы
app.mount("/static", StaticFiles(directory=str(static_directory)), name="static")

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"]
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)


#TODO обьединить с {unprotected_route} в один router
@app.get("/protected-route")
def protected_route(user: User = Depends(current_user)):
    """
        A protected route that returns a greeting to the authenticated user.

        Parameters:
        -----------
        user : User, optional
            The current authenticated user, automatically injected by FastAPI.

        Returns:
        --------
        str
            A greeting message including the username of the authenticated user.
        """

    return f"Hello, {user.username }"



@app.get("/unprotected-route")
def unprotected_route():
    """
        An unprotected route that returns a greeting to any user.

        Returns:
        --------
        str
            A generic greeting message.
        """
    return f"Hello, anonym"



app.include_router(router_car)
app.include_router(router_tasks)
app.include_router(router_pages)
origins =[
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    #разрешены ли браузером отправка учетных данных (например, cookie)
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT","PATCH", "DELETE","OPTIONS"],
    allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers", "Access-Control-Allow-Origin",
                   "Authorization"],

)


@app.on_event("startup")
async def startup():
    redis = aioredis.from_url("redis://localhost")
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")