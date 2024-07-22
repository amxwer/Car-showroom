from fastapi import APIRouter, Depends
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from cars.models import Cars
from cars.schemas import CarsCreate,CarsRead
from auth.connection_database import get_async_session

router = APIRouter(
    prefix="/cars",
    tags=["cars"]

)


@router.get("/")
async def get_cars(brand_type : str,session: AsyncSession = Depends(get_async_session)):
    query = select(Cars).where(Cars.brand == brand_type)
    result = await session.execute(query)
    return result.scalars().all()

@router.post("/")
async def add_cars(new_cars: CarsCreate,session: AsyncSession =Depends(get_async_session)):
    stmt = insert(Cars).values(**new_cars.dict())
    await session.execute(stmt)
    await session.commit()

    return {"status": "cars added"}


