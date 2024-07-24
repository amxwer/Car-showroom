import cache
from fastapi import APIRouter, Depends
from fastapi_cache.decorator import cache
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
@cache(expire=30)
async def get_cars(brand_type : str,session: AsyncSession = Depends(get_async_session)):
    """
        Fetch cars based on the brand type.

        Parameters:
        -----------
        brand_type : str
            The type of the car brand to filter by.
        session : AsyncSession, optional
            The database session used to execute the query, automatically injected by FastAPI.

        Returns:
        --------
        List[Cars]
            A list of cars that match the specified brand type.
        """
    query = select(Cars).where(Cars.brand == brand_type)
    result = await session.execute(query)
    return result.scalars().all()

@router.post("/")
@cache(expire=30)
async def add_cars(new_cars: CarsCreate,session: AsyncSession =Depends(get_async_session)):
    """
        Add a new car to the database.

        Parameters:
        -----------
        new_cars : CarsCreate
            The data for the new car to be added.
        session : AsyncSession, optional
            The database session used to execute the insert statement, automatically injected by FastAPI.

        Returns:
        --------
        dict
            A confirmation message indicating the status of the operation.
        """
    stmt = insert(Cars).values(**new_cars.dict())
    await session.execute(stmt)
    await session.commit()

    return {"status": "cars added"}


