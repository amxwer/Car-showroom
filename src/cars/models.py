#TODO:придумать методы и поля для взаимодействия с машинами
import enum

from sqlalchemy import Table, MetaData, Integer, Column, Enum, String, Float
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase

from database import metadata

class Base(DeclarativeBase):
    metadata = metadata


class CarBrand(str, enum.Enum):
    """
       Enumeration for car brands.

       Attributes:
       -----------
       VW : str
           Volkswagen brand.
       SEAT : str
           SEAT brand.
       """
    VW = "VOLKSWAGEN"
    SEAT = "SEAT"


class VWModel(str, enum.Enum):
    """
      Enumeration for Volkswagen car models.

      Attributes:
      -----------
      ARTEON : str
          Volkswagen Arteon model.
      GOLF : str
          Volkswagen Golf model.
      TIGUAN : str
          Volkswagen Tiguan model.
      TOUREG : str
          Volkswagen Touareg model.
      """
    ARTEON = "ARTEON"
    GOLF = "GOLF"
    TIGUAN = "TIGUAN"
    TOUREG = "TOUREG"


class SeatModel(str, enum.Enum):
    """
        Enumeration for SEAT car models.

        Attributes:
        -----------
        LEON : str
            SEAT Leon model.
        IBIZA : str
            SEAT Ibiza model.
        MII : str
            SEAT Mii model.
        ATECA : str
            SEAT Ateca model.
        """
    LEON = "LEON"
    IBIZA = "IBIZA"
    MII = "MII"
    ATECA = "ATECA"


class CarType(str, enum.Enum):
    """
       Enumeration for car types.

       Attributes:
       -----------
       SEDAN : str
           Sedan car type.
       LIFTBACK : str
           Liftback car type.
       HATCHBACK : str
           Hatchback car type.
       SUV : str
           SUV car type.
       """
    SEDAN = "Sedan"
    LIFTBACK = "Liftback"
    HATCHBACK = "Hatchback"
    SUV = "SUV"


class GearBoxType(str, enum.Enum):
    """
       Enumeration for gearbox types.

       Attributes:
       -----------
       MANUAL : str
           Manual gearbox.
       AUTOMATIC : str
           Automatic gearbox.
       """
    MANUAL = "MANUAL"
    AUTOMATIC = "AUTOMATIC"

class ConfigCar(str, enum.Enum):
    """
        Enumeration for car configurations.

        Attributes:
        -----------
        BASIC : str
            Basic configuration.
        COMFORT : str
            Comfort configuration.
        SPORT : str
            Sport configuration.
        PREMIUM : str
            Premium configuration.
        """

    BASIC = "BASIC"
    COMFORT = "COMFORT"
    SPORT = "SPORT"
    PREMIUM = "PREMIUM"





class Cars(Base):
    """
        ORM class representing a car in the database.

        Attributes:
        -----------
        id : int
            Primary key, unique identifier for each car.
        brand : CarBrand
            The brand of the car (e.g., Volkswagen, SEAT).
        model : str
            The model of the car.
        year_of_release : int
            The year the car was released.
        price : int
            The price of the car.
        engine_capacity : float
            The engine capacity of the car.
        gearbox : GearBoxType
            The type of gearbox the car has.
        type_car : CarType
            The type of the car (e.g., Sedan, SUV).
        power : int
            The power of the car in horsepower.
        car_config : ConfigCar
            The configuration of the car (e.g., Basic, Sport).

        Methods:
        --------
        set_model(model):
            Sets the model of the car based on its brand. Raises a ValueError if the model is not valid for the brand.
        """
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