from typing import List
from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from models.database import get_db
from models.holedata.offset_model import OffsetBase, OffsetDisplayBase, OffsetLotDisplay

from routers.holedata import offset_controller

router = APIRouter(prefix="/offset", tags=["offset"])


@router.get("/", response_model=List[OffsetDisplayBase])
def get_all_calibrationdata(db: Session = Depends(get_db)):
    return offset_controller.read_offsetdata(db)



@router.get("/last_start{start}:end{end}", response_model=List[OffsetDisplayBase])
def get_last_calibration(start: str, end: str, db: Session = Depends(get_db)):
    return offset_controller.read_offset_last(db, start, end)


@router.get("/{id}")
def calibration_by_id(id: int, db:Session=Depends(get_db)):
    return offset_controller.read_offsetdata_by_id(db, id)



@router.get("/calibrationlotgroup/", response_model=List[OffsetLotDisplay])
def lotgroup(db: Session=Depends(get_db)):
    return offset_controller.offsetlot_group(db)


@router.get("/calibrationbylot/{lot}", response_model=List[OffsetDisplayBase])
def rankdatabyproduct_lot(lot:str, db:Session=Depends(get_db)):
    return offset_controller.offsetdataby_lot(db, lot)



@router.post("/")
def create_sensor(request: OffsetBase, db: Session = Depends(get_db)):
    return offset_controller.create(db, request)



@router.delete("/{id}")
def delete_api(id: int, db:Session=Depends(get_db)):
    return offset_controller.delete(db, id)
