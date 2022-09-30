from multiprocessing import Event
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from sqlalchemy.sql import func
from datetime import datetime, timedelta

from models.machine.runtime_model import DbRuntimeData, RuntimeBase
from fastapi import HTTPException, status

def create(db: Session, request: RuntimeBase):
    new_runtime = DbRuntimeData(
        Date=request.Date,
        Hour = request.Hour,
        Run=request.Run,
        Stop=request.Stop,
        EventA=request.EventA,
        EventB=request.EventB,
        EventC=request.EventC,
        EventD=request.EventD,
        EventE=request.EventE,
        Remark=request.Remark
    )
    db.add(new_runtime)
    db.commit()
    db.refresh(new_runtime)
    return new_runtime



def read_statusdata(db: Session):
    return db.query(DbRuntimeData).all()

 
def read_status_by_id(db: Session, id: int):
    return db.query(DbRuntimeData).filter(DbRuntimeData.id == id).first()

def read_runtime_last(db: Session, start: str, end: str):
    NOW = datetime.utcnow()
    return db.query(DbRuntimeData).filter(DbRuntimeData.created_date.between(start, end)).all()
