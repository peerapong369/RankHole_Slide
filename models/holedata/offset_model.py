from enum import unique
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String, DateTime, DECIMAL, FLOAT
from sqlalchemy.sql import func
from datetime import datetime

from typing import List

from decimal import Decimal
from models.database import Base
from pydantic import BaseModel

class DbOffetData(Base):
    __tablename__ = "offset"
    id = Column(Integer, primary_key=True, index=True)
    Product =  Column(String, unique=False)
    cal_lot =  Column(String, unique=False)
    LA =  Column(FLOAT, unique=False)
    LB =  Column(FLOAT, unique=False)
    LC =  Column(FLOAT, unique=False)
    LD =  Column(FLOAT, unique=False)
    WA =  Column(FLOAT, unique=False)
    WB =  Column(FLOAT, unique=False)
    WC =  Column(FLOAT, unique=False)
    WD =  Column(FLOAT, unique=False)
    cal_pass = Column(Integer, unique=False)
    created_date = Column(DateTime, default=datetime.now)

class OffsetBase(BaseModel):
    Product : str
    cal_lot : str
    LA : float
    LB : float
    LC : float
    LD : float
    WA : float
    WB : float
    WC : float
    WD : float
    cal_pass : int

class OffsetDisplayBase(BaseModel):
    id: int
    Product : str
    cal_lot : str
    LA : float
    LB : float
    LC : float
    LD : float
    WA : float
    WB : float
    WC : float
    WD : float
    cal_pass : int
    created_date: datetime

    class Config:
        orm_mode = True

class OffsetLotDisplay(BaseModel):
    cal_lot: str

    class Config:
        orm_mode = True