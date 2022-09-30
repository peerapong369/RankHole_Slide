from typing import List
from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from models.database import get_db
from models.machine.status_model import StatusBase, StatusDisplayBase

from routers.machine import status_controller

router = APIRouter(prefix="/status", tags=["status"])


@router.get("/", response_model=List[StatusDisplayBase])
def get_all_calibrationdata(db: Session = Depends(get_db)):
    return status_controller.read_statusdata(db)



@router.get("/{id}")
def calibration_by_id(id: int, db:Session=Depends(get_db)):
    return status_controller.read_status_by_id(db, id)



@router.post("/")
def create_sensor(request: StatusBase, db: Session = Depends(get_db)):
    return status_controller.create(db, request)


@router.put("/{id}")
def put_api(id: int, request:StatusBase, db:Session=Depends(get_db)):
    return status_controller.update(db, id, request)