from cProfile import label
from itertools import groupby
from turtle import speed
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from sqlalchemy.sql import func, text
from datetime import datetime, timedelta

from models.holedata.holedatachange_model import DbHoledataChange, HoledataChangeBase


def create(db: Session, request: HoledataChangeBase):
    new_holedata_change = DbHoledataChange(
        Date=request.Date,
        Product=request.Product,
        LOT=request.LOT,
        Total=request.Total,
        Start = request.Start,
        End = request.End,
        Hrs = request.Hrs,
        Run = request.Run,
        Stop = request.Stop,
        Changeto = request.Changeto
    )
    db.add(new_holedata_change)
    db.commit()
    db.refresh(new_holedata_change)
    return new_holedata_change


def delete(db: Session, id: int):
    sensor = db.query(DbHoledataChange).filter(DbHoledataChange.id == id).first()
    db.delete(sensor)
    db.commit()
    return JSONResponse(content={"detail": f"Sensor id {id} deleted"})


def read_holedata(db: Session):
    return db.query(DbHoledataChange).all()


def read_holedata_last(db: Session, start: str, end: str):
    NOW = datetime.utcnow()
    return db.query(DbHoledataChange).filter(DbHoledataChange.created_date.between(start, end)).all()

 
def read_holedata_by_id(db: Session, id: int):
    return db.query(DbHoledataChange).filter(DbHoledataChange.id == id).first()



def groupby_lot(db:Session):
    return db.query(
        DbHoledataChange.created_date.label('ChangeDate'),
        DbHoledataChange.Date.label('Date'),
        DbHoledataChange.Product.label('product'),
        DbHoledataChange.LOT.label('Lot'),
        DbHoledataChange.Total.label('Total'),
        DbHoledataChange.Start.label('Start'),
        DbHoledataChange.End.label('End'),
        DbHoledataChange.Hrs.label('Hrs'),
        DbHoledataChange.Run.label('Run'),
        DbHoledataChange.Stop.label('Stop'),
        DbHoledataChange.Changeto.label('Changeto'),
    ).group_by(
        DbHoledataChange.LOT,
        DbHoledataChange.Start,
        DbHoledataChange.End
    ).order_by(
        func.max(DbHoledataChange.id).desc()
    ).all()