from enum import Enum

from pydantic import BaseModel, Field, field_validator, root_validator, model_validator, ConfigDict


class CarBrand(str, Enum):
    VW = "VOLKSWAGEN"
    SEAT = "SEAT"


class VWModel(str, Enum):
    ARTEОН = "ARTEON"
    GOLF = "GOLF"
    TIGUAN = "TIGUAN"
    TOUREG = "TOUREG"


class SeatModel(str, Enum):
    LEON = "LEON"
    IBIZA = "IBIZA"
    MII = "MII"
    ATECA = "ATECA"


class CarType(str, Enum):
    SEDAN = "Sedan"
    LIFTBACK = "Liftback"
    HATCHBACK = "Hatchback"
    SUV = "SUV"



class GearBoxType(str, Enum):
    MANUAL = "MANUAL"
    AUTOMATIC = "AUTOMATIC"


class ConfigCar(str, Enum):
    BASIC = "BASIC"
    COMFORT = "COMFORT"
    SPORT = "SPORT"
    PREMIUM = "PREMIUM"



class CarsRead(BaseModel):
    brand: CarBrand
    model: str
    year_of_release: int
    price: int
    engine_capacity: float
    gearbox: GearBoxType
    type_car: CarType
    power: int
    car_config: ConfigCar

    class Config:
        model_config = ConfigDict(from_attributes=True)








class CarsCreate(BaseModel):
    brand :CarBrand
    model : str
    year_of_release :int = Field(ge=2016,le=2023)
    price : int = Field(ge=10000,le=2000000)
    engine_capacity :float = Field(ge=1.0,le=3.0)
    gearbox :GearBoxType
    type_car:CarType
    power: int = Field(ge=80,le=400)
    car_config :ConfigCar

    @model_validator(mode='before')
    def validate_model(cls, values):
        """
                Validate the model of the car based on the brand.

                Parameters:
                -----------
                values : dict
                    The dictionary of values to be validated.

                Raises:
                -------
                ValueError
                    If the model is not valid for the brand.
                """
        brand = values.get('brand')
        model = values.get('model')

        if brand == CarBrand.VW:
            if model not in [m.value for m in VWModel]:
                raise ValueError(f"Invalid model '{model}' for brand {brand}")
        elif brand == CarBrand.SEAT:
            if model not in [m.value for m in SeatModel]:
                raise ValueError(f"Invalid model '{model}' for brand {brand}")
        else:
            raise ValueError(f"Brand {brand} does not support models")
        return values


    class Config:
        use_enum_values = True


    #TODO: добавить для чтения и создания машин