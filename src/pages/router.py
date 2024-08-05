from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from cars.router import get_cars
import logging
router = APIRouter(
    tags=['pages'],
    prefix="/pages"
)


templates = Jinja2Templates(directory="templates")


@router.get("/search/{brand_type}")
def get_search_page(request:Request,cars = Depends(get_cars)):
    logging.debug(cars)

    return templates.TemplateResponse("search.html", {"request":request,"cars":cars["data"]})