from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from sqlalchemy.sql import func
from datetime import datetime, timedelta

from models.machine.calibration_alarm_model import DbCalAlarmData, CalAlarmBase
from fastapi import HTTPException, status

def create(db: Session, request: CalAlarmBase):
    new_calalarm = DbCalAlarmData(
        Product=request.Product,
        Lot = request.Lot,
        Remark=request.Remark,
    )
    db.add(new_calalarm)
    db.commit()
    db.refresh(new_calalarm)
    return new_calalarm



def read_calalarmdata(db: Session):
    return db.query(DbCalAlarmData).all()

 
def read_calalarmdatay_id(db: Session, id: int):
    return db.query(DbCalAlarmData).filter(DbCalAlarmData.id == id).first()


def calalarmdata_last(db: Session, start: str, end: str):
    NOW = datetime.utcnow()
    return db.query(DbCalAlarmData).filter(DbCalAlarmData.created_date.between(start, end)).all()