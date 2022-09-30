from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String, DateTime, DECIMAL, FLOAT
from sqlalchemy.sql import func
from datetime import datetime

from typing import List

from decimal import Decimal
from models.database import Base
from pydantic import BaseModel

class DbCalibrationHoleData(Base):
    __tablename__ = "calibration"
    id = Column(Integer, primary_key=True, index=True)
    Product =  Column(String, unique=False)
    LOT =  Column(String, unique=False)
    sheet = Column(Integer, unique=False)
    round = Column(Integer, unique=False)
    LA =  Column(FLOAT, unique=False)
    LB =  Column(FLOAT, unique=False)
    LC =  Column(FLOAT, unique=False)
    LD =  Column(FLOAT, unique=False)
    WA =  Column(FLOAT, unique=False)
    WB =  Column(FLOAT, unique=False)
    WC =  Column(FLOAT, unique=False)
    WD =  Column(FLOAT, unique=False)
    created_date = Column(DateTime, default=datetime.now)

class CalibrationBase(BaseModel):
    Product : str
    LOT : str
    sheet : int
    round : int
    LA : float
    LB : float
    LC : float
    LD : float
    WA : float
    WB : float
    WC : float
    WD : float

class CalibrationDisplayBase(BaseModel):
    id: int
    Product : str
    LOT : str
    sheet : int
    round : int
    LA : float
    LB : float
    LC : float
    LD : float
    WA : float
    WB : float
    WC : float
    WD : float
    created_date: datetime

    class Config:
        orm_mode = True

class CalLotDisplay(BaseModel):
    LOT: str

    class Config:
        orm_mode = True