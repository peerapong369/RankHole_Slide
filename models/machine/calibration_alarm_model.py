from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String, DateTime, DECIMAL, FLOAT
from sqlalchemy.sql import func
from datetime import datetime

from typing import List

from decimal import Decimal
from models.database import Base
from pydantic import BaseModel

class DbCalAlarmData(Base):
    __tablename__ = "Calibration_Alarm"
    id = Column(Integer, primary_key=True, index=True)
    created_date = Column(DateTime, default=datetime.now)
    Product =  Column(String, unique=False)
    Lot =  Column(String, unique=False)
    Remark = Column(String, unique=False)

class CalAlarmBase(BaseModel):
    Product: str
    Lot : str
    Remark : str

class CalAlarmDisplayBase(BaseModel):
    id: int   
    created_date: datetime
    Product: str
    Lot : str
    Remark : str

    class Config:
        orm_mode = True