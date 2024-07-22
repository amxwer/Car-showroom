from typing import Optional

from fastapi_users import schemas
from pydantic import ConfigDict


class UserRead(schemas.BaseUser[int]):
    """
        UserRead is a data model for reading user information.

        Attributes:
        -----------
        id : int
            Unique identifier for the user.
        email : str
            The email address of the user.
        name : str
            The name of the user.
        username : str
            The username of the user.
        role_id : int
            The identifier for the role assigned to the user.
        is_active : bool, optional
            Indicates whether the user account is active (default is True).
        is_superuser : bool, optional
            Indicates whether the user has superuser privileges (default is False).
        is_verified : bool, optional
            Indicates whether the user's email is verified (default is False).

        Config:
        -------
        model_config : ConfigDict
            Configuration dictionary that sets the attribute source for the model.
        """

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
    """
        UserCreate is a data model for creating a new user.

        Attributes:
        -----------
        username : str
            The username for the new user.
        name : str
            The name of the new user.
        email : str
            The email address of the new user.
        password : str
            The password for the new user.
        role_id : int
            The identifier for the role assigned to the new user.
        is_active : Optional[bool], optional
            Indicates whether the user account is active (default is True).
        is_superuser : Optional[bool], optional
            Indicates whether the user has superuser privileges (default is False).
        is_verified : Optional[bool], optional
            Indicates whether the user's email is verified (default is False).
        """
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