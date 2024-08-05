import datetime
from datetime import datetime

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import  Table, Column, String, Integer, JSON, TIMESTAMP, ForeignKey, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from database import Base,metadata



#TODO переделать orm классы
role = Table(
    'role',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(255), nullable=False),
    Column("permissions",JSON)

)


#TODO переделать orm классы
user = Table(
    "user",
    metadata,

    Column('id', Integer, primary_key=True),
    Column('name', String(255), nullable=False),
    Column("username", String(255), nullable=False),
    Column('email',String(255), nullable=False),
    Column("hashed_password", String(255), nullable=False),
    Column("registered_at",TIMESTAMP,default=datetime.utcnow),
    Column("role_id",Integer, ForeignKey(role.c.id)),
    Column("is_active",Boolean,default=True,nullable=False),
    Column("is_superuser",Boolean,default=False,nullable=False),
    Column("is_verified",Boolean,default=False,nullable=False),

)


class User(SQLAlchemyBaseUserTable[int], Base):
    id:Mapped[int] = mapped_column(
        'id', Integer, primary_key=True
    )
    name:Mapped[str] = mapped_column(
        'name', String(255), nullable=False
    )
    username:Mapped[str] = mapped_column (
        "username", String(255), nullable=False
    )
    email: Mapped[str] = mapped_column(
        String(length=320), unique=True, index=True, nullable=False
    )
    hashed_password: Mapped[str] = mapped_column(
        String(length=1024), nullable=False
    )
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False
    )
    is_verified: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False
    )
    registered_at:Mapped[TIMESTAMP] = mapped_column(
        "registered_at", TIMESTAMP, default=datetime.utcnow
    )
    role_id:Mapped[Integer] = mapped_column(
        "role_id", Integer, ForeignKey(role.c.id)
    )
