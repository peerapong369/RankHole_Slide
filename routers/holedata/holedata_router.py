from typing import List
from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from models.database import get_db
from models.holedata.holedata_model import HoledataBase, HoledataDisplayBase, ProductGroupDisplay, ProductLotDisplay

from routers.holedata import holedata_controller

router = APIRouter(prefix="/holedata", tags=["holedata"])


@router.get("/", response_model=List[HoledataDisplayBase])
def get_all_sensor(db: Session = Depends(get_db)):
    return holedata_controller.read_holedata(db)



@router.get("/last_start{start}:end{end}", response_model=List[HoledataDisplayBase])
def get_last_sensor(start: str, end: str, db: Session = Depends(get_db)):
    return holedata_controller.read_holedata_last(db, start, end)


@router.get("/{id}")
def sensor_by_id(id: int, db:Session=Depends(get_db)):
    return holedata_controller.read_holedata_by_id(db, id)


@router.get("/hole_productgroup/", response_model=List[ProductGroupDisplay])
def productgroup(db: Session=Depends(get_db)):
    return holedata_controller.product_group(db)

@router.get("/hole_lotgroup/{product}", response_model=List[ProductLotDisplay])
def lotgroup(product:str, db: Session=Depends(get_db)):
    return holedata_controller.productlot_group(db, product)


@router.get("/holedataby/{product},{lot}", response_model=List[HoledataDisplayBase])
def rankdatabyproduct_lot(product:str, lot:str, db:Session=Depends(get_db)):
    return holedata_controller.databygroup_lot(db, product, lot)


@router.get("/holedataanalysisby/{product},{lot},{sheet}")
def rankdatabyproduct_lot(product:str, lot:str, sheet:float,db:Session=Depends(get_db)):
    return holedata_controller.databygroup_lot_analysis(db, product, lot, sheet)


@router.get("/lotsummarybyprod/{product}")
def lotsummarybyproduct(product:str, db:Session=Depends(get_db)):
    return holedata_controller.machineresultby_prod(db,product)


@router.get("/lotsummarryperhour/{product},{lot}")
def lotsummaryperhour(product:str, lot:str, db:Session=Depends(get_db)):
    return holedata_controller.prodlotresultperhour(db, product, lot)


@router.get("/lotsummarrypermin/{product},{lot},{Date},{hour}")
def lotsummarypermin(product:str, lot:str, Date:str, hour:str, db:Session=Depends(get_db)):
    return holedata_controller.prodlotresultpermin(db, product, lot, Date, hour)

@router.get("/lotsummarrygroupdate/{product},{lot}")
def lotsummarygroupdate(product:str, lot:str, db:Session=Depends(get_db)):
    return holedata_controller.prodlotresultperhour_gruopdate(db, product, lot)

@router.post("/")
def create_sensor(request: HoledataBase, db: Session = Depends(get_db)):
    return holedata_controller.create(db, request)



@router.delete("/{id}")
def delete_api(id: int, db:Session=Depends(get_db)):
    return holedata_controller.delete(db, id)
