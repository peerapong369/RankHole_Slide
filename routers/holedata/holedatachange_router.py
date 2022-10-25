from typing import List
from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from models.database import get_db
from models.holedata.holedatachange_model import HoledataChangeBase, HoledataChangeDisplayBase

from routers.holedata import holedatachange_controller

router = APIRouter(prefix="/holedatachange", tags=["holedatachange"])


@router.get("/", response_model=List[HoledataChangeDisplayBase])
def get_all_holedatachange(db: Session = Depends(get_db)):
    return holedatachange_controller.read_holedata(db)



@router.get("/last_start{start}:end{end}", response_model=List[HoledataChangeDisplayBase])
def get_last_holedatachange(start: str, end: str, db: Session = Depends(get_db)):
    return holedatachange_controller.read_holedata_last(db, start, end)


@router.get("/lastupdatebylot/")
def get_lastupdatebylot(db:Session=Depends(get_db)):
    return holedatachange_controller.groupby_lot(db)


@router.get("/{id}")
def holedatachange_by_id(id: int, db:Session=Depends(get_db)):
    return holedatachange_controller.read_holedata_by_id(db, id)



@router.post("/")
def create_holedatachange(request: HoledataChangeBase, db: Session = Depends(get_db)):
    return holedatachange_controller.create(db, request)



@router.delete("/{id}")
def delete_api(id: int, db:Session=Depends(get_db)):
    return holedatachange_controller.delete(db, id)
