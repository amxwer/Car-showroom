from fastapi import FastAPI, Depends

from auth.base_config import current_user, fastapi_users, auth_backend
from auth.models import User
from auth.schemas import UserRead, UserCreate
from cars.router import router as router_car

app = FastAPI(
    title = "app",
    debug=True
)

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



@app.get("/protected-route")
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.username }"

@app.get("/unprotected-route")
def unprotected_route():
    return f"Hello, anonym"


app.include_router(router_car)