from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String, DateTime, DECIMAL, FLOAT
from sqlalchemy.sql import func
from datetime import datetime

from typing import List

from decimal import Decimal
from models.database import Base
from pydantic import BaseModel

class DbHoledata(Base):
    __tablename__ = "holedatatable"
    id = Column(Integer, primary_key=True, index=True)
    Product =  Column(String, unique=False)
    LOT =  Column(String, unique=False)
    LA =  Column(FLOAT, unique=False)
    LB =  Column(FLOAT, unique=False)
    LC =  Column(FLOAT, unique=False)
    LD =  Column(FLOAT, unique=False)
    WA =  Column(FLOAT, unique=False)
    WB =  Column(FLOAT, unique=False)
    WC =  Column(FLOAT, unique=False)
    WD =  Column(FLOAT, unique=False)
    HA =  Column(FLOAT, unique=False)
    HB =  Column(FLOAT, unique=False)
    HC =  Column(FLOAT, unique=False)
    HD =  Column(FLOAT, unique=False)
    OfsetLA =  Column(FLOAT, unique=False)
    OfsetLB =  Column(FLOAT, unique=False)
    OfsetLC =  Column(FLOAT, unique=False)
    OfsetLD =  Column(FLOAT, unique=False)
    OfsetWA =  Column(FLOAT, unique=False)
    OfsetWB =  Column(FLOAT, unique=False)
    OfsetWC =  Column(FLOAT, unique=False)
    OfsetWD =  Column(FLOAT, unique=False)
    A_Llowlimit =  Column(FLOAT, unique=False)
    A_Luplimit =  Column(FLOAT, unique=False)
    A_Wlowlimit =  Column(FLOAT, unique=False)
    A_Wuplimit =  Column(FLOAT, unique=False)
    B_Llowlimit =  Column(FLOAT, unique=False)
    B_Luplimit =  Column(FLOAT, unique=False)
    B_Wlowlimit =  Column(FLOAT, unique=False)
    B_Wuplimit =  Column(FLOAT, unique=False)
    C_Llowlimit =  Column(FLOAT, unique=False)
    C_Luplimit =  Column(FLOAT, unique=False)
    C_Wlowlimit =  Column(FLOAT, unique=False)
    C_Wuplimit =  Column(FLOAT, unique=False)
    D_Llowlimit =  Column(FLOAT, unique=False)
    D_Luplimit =  Column(FLOAT, unique=False)
    D_Wlowlimit =  Column(FLOAT, unique=False)
    D_Wuplimit =  Column(FLOAT, unique=False)
    AL_Spec =  Column(FLOAT, unique=False)
    BL_Spec =  Column(FLOAT, unique=False)
    CL_Spec =  Column(FLOAT, unique=False)
    DL_Spec =  Column(FLOAT, unique=False)
    AW_Spec =  Column(FLOAT, unique=False)
    BW_Spec =  Column(FLOAT, unique=False)
    CW_Spec =  Column(FLOAT, unique=False)
    DW_Spec =  Column(FLOAT, unique=False)
    HoleSlide =  Column(Integer, unique=False)
    HoleSize =  Column(Integer, unique=False)
    DBSnap =  Column(Integer, unique=False)
    Recheck =  Column(Integer, unique=False)
    speed = Column(FLOAT, unique=False)
    created_date = Column(DateTime, default=datetime.now)
    update_date = Column(
        DateTime, nullable=False, default=datetime.now, onupdate=datetime.now
    )

class HoledataBase(BaseModel):
    Product : str
    LOT : str
    LA : float
    LB : float
    LC : float
    LD : float
    WA : float
    WB : float
    WC : float
    WD : float
    HA : float
    HB : float
    HC : float
    HD : float
    OfsetLA : float
    OfsetLB : float
    OfsetLC : float
    OfsetLD : float
    OfsetWA : float
    OfsetWB : float
    OfsetWC : float
    OfsetWD : float
    A_Llowlimit : float
    A_Luplimit : float
    A_Wlowlimit : float
    A_Wuplimit : float
    B_Llowlimit : float
    B_Luplimit : float
    B_Wlowlimit : float
    B_Wuplimit : float
    C_Llowlimit : float
    C_Luplimit : float
    C_Wlowlimit : float
    C_Wuplimit : float
    D_Llowlimit : float
    D_Luplimit : float
    D_Wlowlimit : float
    D_Wuplimit : float
    AL_Spec : float
    BL_Spec : float
    CL_Spec : float
    DL_Spec : float
    AW_Spec : float
    BW_Spec : float
    CW_Spec : float
    DW_Spec : float
    HoleSlide : int
    HoleSize : int
    DBSnap : int
    Recheck : int
    speed : float



class HoledataDisplayBase(BaseModel):
    id: int
    Product : str
    LOT : str
    LA : float
    LB : float
    LC : float
    LD : float
    WA : float
    WB : float
    WC : float
    WD : float
    HA : float
    HB : float
    HC : float
    HD : float
    OfsetLA : float
    OfsetLB : float
    OfsetLC : float
    OfsetLD : float
    OfsetWA : float
    OfsetWB : float
    OfsetWC : float
    OfsetWD : float
    A_Llowlimit : float
    A_Luplimit : float
    A_Wlowlimit : float
    A_Wuplimit : float
    B_Llowlimit : float
    B_Luplimit : float
    B_Wlowlimit : float
    B_Wuplimit : float
    C_Llowlimit : float
    C_Luplimit : float
    C_Wlowlimit : float
    C_Wuplimit : float
    D_Llowlimit : float
    D_Luplimit : float
    D_Wlowlimit : float
    D_Wuplimit : float
    AL_Spec : float
    BL_Spec : float
    CL_Spec : float
    DL_Spec : float
    AW_Spec : float
    BW_Spec : float
    CW_Spec : float
    DW_Spec : float
    HoleSlide : int
    HoleSize : int
    DBSnap : int
    Recheck : int
    speed : float
    created_date: datetime
    update_date: datetime

    class Config:
        orm_mode = True



class ProductGroupDisplay(BaseModel):
    Product: str

    class Config:
        orm_mode = True

class ProductLotDisplay(BaseModel):
    LOT: str

    class Config:
        orm_mode = True

