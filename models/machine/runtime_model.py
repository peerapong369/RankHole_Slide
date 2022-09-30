from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String, DateTime, DECIMAL, FLOAT
from sqlalchemy.sql import func
from datetime import datetime

from typing import List

from decimal import Decimal
from models.database import Base
from pydantic import BaseModel

class DbRuntimeData(Base):
    __tablename__ = "Machine_runtime"
    id = Column(Integer, primary_key=True, index=True)
    Date = Column(String, unique=False)
    Hour = Column(Integer, unique=False)
    Run =  Column(Integer, unique=False)
    Stop =  Column(Integer, unique=False)
    EventA = Column(Integer, unique=False)
    EventB = Column(Integer, unique=False)
    EventC = Column(Integer, unique=False)
    EventD = Column(Integer, unique=False)
    EventE = Column(Integer, unique=False)
    Remark  = Column(String, unique=False)
    created_date = Column(DateTime, default=datetime.now)

class RuntimeBase(BaseModel):
    Date : str
    Hour : int
    Run : int
    Stop : int
    EventA : int
    EventB : int
    EventC : int
    EventD : int
    EventE : int
    Remark : str

class RuntimeDisplayBase(BaseModel):
    id: int
    Date : str
    Hour : int
    Run : int
    Stop : int
    EventA : int
    EventB : int
    EventC : int
    EventD : int
    EventE : int
    Remark : str    
    created_date: datetime

    class Config:
        orm_mode = True