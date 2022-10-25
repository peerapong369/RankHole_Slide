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


@router.get("machinedatabylot/speed{speed}/between{start}:end{end}")
def get_last_sensor(speed:float ,start: str, end: str, db: Session = Depends(get_db)):
    return holedata_controller.machineresultby_datetime(db, speed, start, end)


@router.get("machinedatabyhour/speed{speed}/between{start}:end{end}")
def get_last_sensor(speed:float ,start: str, end: str, db: Session = Depends(get_db)):
    return holedata_controller.machineresultby_datetime_hour(db, speed, start, end)


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


@router.get("/holedataanalysisby/{lot},{sheet}")
def rankdatabyproduct_lot(lot:str, sheet:float,db:Session=Depends(get_db)):
    return holedata_controller.databygroup_lot_analysis(db, lot, sheet)


@router.get("/lotsummarybyprod/{product}")
def lotsummarybyproduct(product:str, db:Session=Depends(get_db)):
    return holedata_controller.machineresultby_prod(db,product)


@router.get("/lotsummarryperhour/{lot}")
def lotsummaryperhour(lot:str, db:Session=Depends(get_db)):
    return holedata_controller.prodlotresultperhour(db, lot)


@router.get("/lotsummarrypermin/{lot},{Date},{hour}")
def lotsummarypermin(lot:str, Date:str, hour:str, db:Session=Depends(get_db)):
    return holedata_controller.prodlotresultpermin(db, lot, Date, hour)

@router.get("/lotsummarrygroupdate/{lot}")
def lotsummarygroupdate(lot:str, db:Session=Depends(get_db)):
    return holedata_controller.prodlotresultperhour_gruopdate(db, lot)


@router.get("/productivitybydate/start{start}end{end}speed{speed}")
def productivitybydate(start:str, end:str, speed:float, db:Session=Depends(get_db)):
    return holedata_controller.productivity_bydate(start, end, speed, db)


@router.post("/")
def create_sensor(request: HoledataBase, db: Session = Depends(get_db)):
    return holedata_controller.create(db, request)



@router.delete("/{id}")
def delete_api(id: int, db:Session=Depends(get_db)):
    return holedata_controller.delete(db, id)
