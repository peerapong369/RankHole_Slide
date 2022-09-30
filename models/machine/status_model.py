from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String, DateTime, DECIMAL, FLOAT
from sqlalchemy.sql import func
from datetime import datetime

from typing import List

from decimal import Decimal
from models.database import Base
from pydantic import BaseModel

class DbStatusData(Base):
    __tablename__ = "Machine_status"
    id = Column(Integer, primary_key=True, index=True)
    Status_str = Column(String, unique=False)
    Status = Column(Integer, unique=False)
    Product =  Column(String, unique=False)
    LOT =  Column(String, unique=False)
    update_date = Column(
        DateTime, nullable=False, default=datetime.now, onupdate=datetime.now
    )

class StatusBase(BaseModel):
    Status_str : str
    Status : int
    Product : str
    LOT : str

class StatusDisplayBase(BaseModel):
    id: int
    Status_str : str
    Status : int
    Product : str
    LOT : str
    update_date: datetime

    class Config:
        orm_mode = True