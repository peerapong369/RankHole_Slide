from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String, DateTime, DECIMAL, FLOAT
from sqlalchemy.sql import func
from datetime import datetime

from typing import List

from decimal import Decimal
from models.database import Base
from pydantic import BaseModel

class DbHoledataChange(Base):
    __tablename__ = "holedatachangetable"
    id = Column(Integer, primary_key=True, index=True)
    Date = Column(String, unique=False)
    Product =  Column(String, unique=False)
    LOT =  Column(String, unique=False)
    Total = Column(Integer, unique=False)
    Start = Column(Integer, unique=False)
    End = Column(Integer, unique=False)
    Hrs = Column(Integer, unique=False)
    Run = Column(FLOAT, unique=False)
    Stop = Column(FLOAT, unique=False)
    Changeto = Column(String, unique=False)
    created_date = Column(DateTime, default=datetime.now)

class HoledataChangeBase(BaseModel):
    Date : str
    Product : str
    LOT : str
    Total : int
    Start : int
    End : int
    Hrs : int
    Run : float
    Stop : float
    Changeto : str
    



class HoledataChangeDisplayBase(BaseModel):
    id: int
    Date : str
    Product : str
    LOT : str
    Total : int
    Start : int
    End : int
    Hrs : int
    Run : float
    Stop : float
    Changeto : str
    created_date: datetime

    class Config:
        orm_mode = True


