#TODO:придумать методы и поля для взаимодействия с машинами
import enum

from sqlalchemy import Table, MetaData, Integer, Column, Enum, String, Float
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase

metadata = MetaData()

class Base(DeclarativeBase):
    metadata = metadata


class CarBrand(str, enum.Enum):
    VW = "VOLKSWAGEN"
    SEAT = "SEAT"


class VWModel(str, enum.Enum):
    ARTEON = "ARTEON"
    GOLF = "GOLF"
    TIGUAN = "TIGUAN"
    TOUREG = "TOUREG"


class SeatModel(str, enum.Enum):
    LEON = "LEON"
    IBIZA = "IBIZA"
    MII = "MII"
    ATECA = "ATECA"


class CarType(str, enum.Enum):
    SEDAN = "Sedan"
    LIFTBACK = "Liftback"
    HATCHBACK = "Hatchback"
    SUV = "SUV"


class GearBoxType(str, enum.Enum):
    MANUAL = "MANUAL"
    AUTOMATIC = "AUTOMATIC"

class ConfigCar(str, enum.Enum):

    BASIC = "BASIC"
    COMFORT = "COMFORT"
    SPORT = "SPORT"
    PREMIUM = "PREMIUM"





class Cars(Base):
    __tablename__ = 'cars'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    brand: Mapped[CarBrand] = mapped_column(Enum(CarBrand), nullable=False)
    model: Mapped[str] = mapped_column(String, nullable=False)
    year_of_release: Mapped[int] = mapped_column(Integer, nullable=False)
    price: Mapped[int] = mapped_column(Integer, nullable=False)
    engine_capacity: Mapped[float] = mapped_column(Float, nullable=False)
    gearbox: Mapped[GearBoxType] = mapped_column(Enum(GearBoxType), nullable=False)
    type_car: Mapped[CarType] = mapped_column(Enum(CarType), nullable=False)
    power: Mapped[int] = mapped_column(Integer, nullable=False)
    car_config: Mapped[ConfigCar] = mapped_column(Enum(ConfigCar), nullable=False)

    def set_model(self, model):
        if self.brand == CarBrand.VW:
            if not isinstance(model, VWModel):
                raise ValueError(f"Invalid model for brand {self.brand}")
            self.model = model.value
        elif self.brand == CarBrand.SEAT:
            if not isinstance(model, SeatModel):
                raise ValueError(f"Invalid model for brand {self.brand}")
            self.model = model.value
        else:
            raise ValueError(f"Brand {self.brand} does not support models")