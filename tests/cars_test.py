from httpx import AsyncClient


async def test_add_cars(ac: AsyncClient):
    response = await ac.post("/cars/add", json={

        "brand": "VOLKSWAGEN",
        "model": "ARTEON",
        "year_of_release": 2018,
        "price": 24000,
        "engine_capacity": 2.0,
        "gearbox": "AUTOMATIC",
        "type_car": "Sedan",
        "power": 190,
        "car_config": "PREMIUM"

    })

    assert response.status_code == 200


async def test_get_cars(ac: AsyncClient):
    response = await ac.get("/cars/find", params={
        "brand_type": "VOLKSWAGEN",
    })
    assert response.status_code == 200
    assert response.json()["status"] == "success"
    assert len(response.json()["data"]) == 1
