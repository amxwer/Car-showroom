from fastapi_users import FastAPIUsers
from fastapi_users.authentication import CookieTransport, JWTStrategy, AuthenticationBackend

from config import SECRET_AUTH
from auth.manager import get_user_manager
from auth.models import User

cookie_transport = CookieTransport(cookie_name="cookie",cookie_max_age=3600)

async def get_user_by_username(username: str):
    user = await user_db.get_by_username(username)
    return user

def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret= SECRET_AUTH,lifetime_seconds=3600)



auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)
fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)
current_user = fastapi_users.current_user()


