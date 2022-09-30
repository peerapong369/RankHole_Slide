from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String, DateTime, DECIMAL
from sqlalchemy.sql import func
from datetime import datetime

from typing import List

from decimal import Decimal
from models.database import Base
from pydantic import BaseModel

class DbSensor(Base):
    __tablename__ = "Sensor"
    id = Column(Integer, primary_key=True, index=True)
    value1 = Column(DECIMAL, unique=False)
    value2 = Column(DECIMAL, unique=False)
    created_date = Column(DateTime, default=datetime.now)
    update_date = Column(
        DateTime, nullable=False, default=datetime.now, onupdate=datetime.now
    )

class SensorBase(BaseModel):
    value1: Decimal
    value2: Decimal


class SensorDisplayBase(BaseModel):
    id: int
    value1: Decimal
    value2: Decimal
    created_date: datetime
    update_date: datetime

    class Config:
        orm_mode = True

class SensorDisplayValue1(BaseModel):
    value1: Decimal

    class Config:
        orm_mode = True

