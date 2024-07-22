from typing import Optional

from fastapi_users import schemas
from pydantic import ConfigDict


class UserRead(schemas.BaseUser[int]):
    id: int
    email: str
    name:str
    username: str
    role_id :int
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False

    class Config:
        model_config = ConfigDict(from_attributes=True)


class UserCreate(schemas.BaseUserCreate):
    username :str
    name:str
    email: str
    password: str
    role_id :int
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False


# class UserUpdate(schemas.BaseUserUpdate):
#     pass