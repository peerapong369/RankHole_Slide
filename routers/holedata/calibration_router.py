from typing import List
from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from models.database import get_db
from models.holedata.calibration_model import CalibrationBase, CalibrationDisplayBase, CalLotDisplay

from routers.holedata import calibration_controller

router = APIRouter(prefix="/calibration", tags=["calibration"])


@router.get("/", response_model=List[CalibrationDisplayBase])
def get_all_calibrationdata(db: Session = Depends(get_db)):
    return calibration_controller.read_calibrationdata(db)



@router.get("/last_start{start}:end{end}", response_model=List[CalibrationDisplayBase])
def get_last_calibration(start: str, end: str, db: Session = Depends(get_db)):
    return calibration_controller.read_calibrationdata_last(db, start, end)


@router.get("/{id}")
def calibration_by_id(id: int, db:Session=Depends(get_db)):
    return calibration_controller.read_calibrationdata_by_id(db, id)



@router.get("/calibrationlotgroup/", response_model=List[CalLotDisplay])
def lotgroup(db: Session=Depends(get_db)):
    return calibration_controller.callot_group(db)


@router.get("/calibrationbylot/{lot}", response_model=List[CalibrationDisplayBase])
def rankdatabyproduct_lot(lot:str, db:Session=Depends(get_db)):
    return calibration_controller.caldataby_lot(db, lot)



@router.post("/")
def create_sensor(request: CalibrationBase, db: Session = Depends(get_db)):
    return calibration_controller.create(db, request)



@router.delete("/{id}")
def delete_api(id: int, db:Session=Depends(get_db)):
    return calibration_controller.delete(db, id)
