from typing import List
from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from models.database import get_db
from models.sensor.sensor_model import SensorBase, SensorDisplayBase, SensorDisplayValue1

from routers.sensor import sensor_controller
from utils.oauth2 import access_user_token

router = APIRouter(prefix="/sensor", tags=["sensor"])


@router.get("/", response_model=List[SensorDisplayBase])
def get_all_sensor(db: Session = Depends(get_db)):
    return sensor_controller.read_sensor(db)


@router.get("/value1", response_model=List[SensorDisplayValue1])
def get_value1_sensor(db: Session = Depends(get_db)):
    return sensor_controller.read_sensor_value1(db)


@router.get("/last_start{start}:end{end}", response_model=List[SensorDisplayBase])
def get_last_sensor(start: str, end: str, db: Session = Depends(get_db)):
    return sensor_controller.read_sensor_last(db, start, end)


@router.get("/{id}")
def sensor_by_id(id: int, db:Session=Depends(get_db)):
    return sensor_controller.read_sensor_by_id(db, id)


@router.post("/")
def create_sensor(request: SensorBase, db: Session = Depends(get_db)):
    return sensor_controller.create(db, request)


@router.put("/{id}")
def put_api(id: int, request:SensorBase, db:Session=Depends(get_db)):
    return sensor_controller.update(db, id, request)


@router.delete("/{id}")
def delete_api(id: int, db:Session=Depends(get_db)):
    return sensor_controller.delete(db, id)
