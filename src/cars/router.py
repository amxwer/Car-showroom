import logging

import cache
from fastapi import APIRouter, Depends,HTTPException
from fastapi_cache.decorator import cache
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from cars.models import Cars
from cars.schemas import CarsCreate,CarsRead
from database import get_async_session

logging.basicConfig(level=logging.DEBUG)
router = APIRouter(
    prefix="/cars",
    tags=["cars"]

)

class Paginator:
    def __init__(self,limit: int = 10,skip: int = 0):
        self.limit = limit
        self.skip = skip


#cache(expire=30)
@router.get("/find")
async def get_cars(brand_type : str,session: AsyncSession = Depends(get_async_session),pagination_params : Paginator = Depends(Paginator)):
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
    try:
        query = select(Cars).where(Cars.brand == brand_type)
        result = await session.execute(query)
        car_list = result.scalars().all()
        logging.info(f'car list: {car_list}')
        return {
            "status": "success",
            "data": car_list,
            "details:":"Cars showroom"
        }
    except Exception:
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": None
        })


#@cache(expire=30)
@router.post("/add")
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
    #TODO добвавить try:except
    stmt = insert(Cars).values(**new_cars.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "cars added"}


