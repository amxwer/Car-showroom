from httpx import AsyncClient
from sqlalchemy import insert, select
from sqlalchemy.exc import IntegrityError

from auth.models import role
from tests.conftest import client, async_session_maker
from tests.conftest import prepare_database


async def test_add_role():
    async with async_session_maker() as session:
        try:
            stmt = insert(role).values(id=1, name="admin", permissions=None)
            await session.execute(stmt)
            await session.commit()
            query = select(role)
            result = await session.execute(query)
            assert result.all() == [(1, 'admin', None)], 'Роль не найдена'


        except IntegrityError:
            print("Integrity error occurred. This may be due to duplicate primary keys or other constraints.")
        #TODO заменить на logging


def test_register():
    response =  client.post("/auth/register", json=
    {
        "email": "string",
        "password": "string",
        "is_active": True,
        "is_superuser": False,
        "is_verified": False,
        "username": "string",
        "name": "string",
        "role_id": 1
    })

    assert response.status_code == 201

def test_login():
    response = client.post("/auth/jwt/login", data={
        "grant_type": "password",
        "username": "string",
        "password": "string",
        "scope": "1",
        "client_id": "1",
        "client_secret": "1"
    })
    assert response.status_code == 204



