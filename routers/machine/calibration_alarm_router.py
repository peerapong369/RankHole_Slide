from typing import List
from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from models.database import get_db
from models.machine.calibration_alarm_model import CalAlarmBase, CalAlarmDisplayBase

from routers.machine import calibration_alarm_controller

router = APIRouter(prefix="/calibrationalarm", tags=["calibrationalarm"])


@router.get("/", response_model=List[CalAlarmDisplayBase])
def get_all_calibrationalarm(db: Session = Depends(get_db)):
    return calibration_alarm_controller.read_calalarmdata(db)



@router.get("/{id}")
def calibration_by_id(id: int, db:Session=Depends(get_db)):
    return calibration_alarm_controller.read_calalarmdatay_id(db, id)

@router.post("/")
def create_calibrationalarm(request: CalAlarmBase, db: Session = Depends(get_db)):
    return calibration_alarm_controller.create(db, request)


@router.get("/last_start{start}:end{end}", response_model=List[CalAlarmDisplayBase])
def get_last_calalarm(start: str, end: str, db: Session = Depends(get_db)):
    return calibration_alarm_controller.calalarmdata_last(db, start, end)