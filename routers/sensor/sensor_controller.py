from tkinter.tix import COLUMN
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from sqlalchemy.sql import func
from datetime import datetime, timedelta

from models.sensor.sensor_model import DbSensor, SensorBase


def create(db: Session, request: SensorBase):
    new_sensor = DbSensor(
        value1=request.value1, 
        value2=request.value2
    )
    db.add(new_sensor)
    db.commit()
    db.refresh(new_sensor)
    return new_sensor


def delete(db: Session, id: int):
    sensor = db.query(DbSensor).filter(DbSensor.id == id).first()
    db.delete(sensor)
    db.commit()
    return JSONResponse(content={"detail": f"Sensor id {id} deleted"})


def update(db: Session, id: int, request: SensorBase):
    sensor = db.query(DbSensor).filter(DbSensor.id == id).first()
    sensor.value1 = request.value1
    sensor.value2 = request.value2
    db.commit()
    db.refresh(sensor)
    return sensor


def read_sensor(db: Session):
    return db.query(DbSensor).all()


def read_sensor_value1(db: Session):
    return db.query(DbSensor).all()


def read_sensor_last(db: Session, start: str, end: str):
    NOW = datetime.utcnow()
    return db.query(DbSensor).filter(DbSensor.created_date.between(start, end)).all()

 
def read_sensor_by_id(db: Session, id: int):
    return db.query(DbSensor).filter(DbSensor.id == id).first()

