from cProfile import label
from itertools import groupby
from turtle import speed
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from sqlalchemy.sql import func, text
from datetime import datetime, timedelta

from models.holedata.holedata_model import DbHoledata, HoledataBase


def create(db: Session, request: HoledataBase):
    new_holedata = DbHoledata(
        Product=request.Product,
        LOT=request.LOT,
        LA=request.LA,
        LB=request.LB,
        LC=request.LC,
        LD=request.LD,
        WA=request.WA,
        WB=request.WB,
        WC=request.WC,
        WD=request.WD,
        HA=request.HA,
        HB=request.HB,
        HC=request.HC,
        HD=request.HD,
        OfsetLA=request.OfsetLA,
        OfsetLB=request.OfsetLB,
        OfsetLC=request.OfsetLC,
        OfsetLD=request.OfsetLD,
        OfsetWA=request.OfsetWA,
        OfsetWB=request.OfsetWB,
        OfsetWC=request.OfsetWC,
        OfsetWD=request.OfsetWD,
        A_Llowlimit=request.A_Llowlimit,
        A_Luplimit=request.A_Luplimit,
        A_Wlowlimit=request.A_Wlowlimit,
        A_Wuplimit=request.A_Wuplimit,
        B_Llowlimit=request.B_Llowlimit,
        B_Luplimit=request.B_Luplimit,
        B_Wlowlimit=request.B_Wlowlimit,
        B_Wuplimit=request.B_Wuplimit,
        C_Llowlimit=request.C_Llowlimit,
        C_Luplimit=request.C_Luplimit,
        C_Wlowlimit=request.C_Wlowlimit,
        C_Wuplimit=request.C_Wuplimit,
        D_Llowlimit=request.D_Llowlimit,
        D_Luplimit=request.D_Luplimit,
        D_Wlowlimit=request.D_Wlowlimit,
        D_Wuplimit=request.D_Wuplimit,
        AL_Spec=request.AL_Spec,
        BL_Spec=request.BL_Spec,
        CL_Spec=request.CL_Spec,
        DL_Spec=request.DL_Spec,
        AW_Spec=request.AW_Spec,
        BW_Spec=request.BW_Spec,
        CW_Spec=request.CW_Spec,
        DW_Spec=request.DW_Spec,
        HoleSlide=request.HoleSlide,
        HoleSize=request.HoleSize,
        DBSnap=request.DBSnap,
        Recheck=request.Recheck,
        speed=request.speed
    )
    db.add(new_holedata)
    db.commit()
    db.refresh(new_holedata)
    return new_holedata


def delete(db: Session, id: int):
    sensor = db.query(DbHoledata).filter(DbHoledata.id == id).first()
    db.delete(sensor)
    db.commit()
    return JSONResponse(content={"detail": f"Sensor id {id} deleted"})


def read_holedata(db: Session):
    return db.query(DbHoledata).all()


def read_holedata_last(db: Session, start: str, end: str):
    NOW = datetime.utcnow()
    return db.query(DbHoledata).filter(DbHoledata.created_date.between(start, end)).all()

 
def read_holedata_by_id(db: Session, id: int):
    return db.query(DbHoledata).filter(DbHoledata.id == id).first()

def product_group(db: Session):
    return db.query(DbHoledata).group_by(DbHoledata.Product).all()

def productlot_group(db: Session, product:str):
    return db.query(
        DbHoledata
    ).filter(
        DbHoledata.Product==product
    ).group_by(
        DbHoledata.LOT
    ).order_by(
        func.max(DbHoledata.created_date).desc()
    ).all()


def databygroup_lot(db: Session, product:str, lot:str):
    return db.query(DbHoledata).filter(DbHoledata.Product==product).filter(DbHoledata.LOT==lot).all()


def databygroup_lot_analysis(db: Session, product:str, lot:str, sheet_permin:float):
    return db.query(
        func.strftime("%Y-%m-%d %H:00:00", DbHoledata.created_date).label('Datetime'),
        func.max(DbHoledata.created_date).label("max_datetime"),
        func.min(DbHoledata.created_date).label("min_datetime"),
        ((func.strftime("%s", func.max(DbHoledata.created_date))-func.strftime("%s", func.min(DbHoledata.created_date)))/60).label("min."),
        (func.sum(
            func.IIf(
                DbHoledata.speed>(sheet_permin*2),
                func.IIf(
                    DbHoledata.speed<=60,
                    DbHoledata.speed,0
                ),
                0
            ))/60
        ).label('Unstable1'),
        (func.sum(
            func.IIf(
                DbHoledata.speed>60,
                func.IIf(
                    DbHoledata.speed<=600,
                    DbHoledata.speed,0
                ),
                0
            ))/60
        ).label('Unstable2'),
        (func.sum(
            func.IIf(
                DbHoledata.speed>600,
                func.IIf(
                    DbHoledata.speed<=3600,
                    DbHoledata.speed,0
                ),
                0
            ))/60
        ).label('minorstop'),
        (func.sum(
            func.IIf(
                DbHoledata.speed>3600,
                func.IIf(
                    DbHoledata.speed<=7200,
                    DbHoledata.speed,0
                ),
                0
            ))/60
        ).label('mainstop'),
        (func.sum(
            func.IIf(
                DbHoledata.speed>7200,DbHoledata.speed,0
            ))/60
        ).label('breakdown'),
    ).filter(
        DbHoledata.Product==product
    ).filter(
        DbHoledata.LOT==lot
    ).group_by(
        func.strftime("%Y-%m-%d %H:00:00", DbHoledata.created_date)
    ).all()
    


def machineresultby_prod(db: Session, product:str):
    return db.query(
        DbHoledata.LOT.label('lot'),
        func.count(DbHoledata.id).label('Total'),
        func.min(DbHoledata.created_date).label('Start_date'),
        func.max(DbHoledata.created_date).label('End_date'),
        (func.count(DbHoledata.id) - (func.sum(DbHoledata.HoleSlide)+func.sum(DbHoledata.HoleSize)+func.sum(DbHoledata.DBSnap)+func.sum(DbHoledata.Recheck))).label('OK'),
        func.sum(DbHoledata.HoleSlide).label('NG_Hole_Slide'),
        func.sum(DbHoledata.HoleSize).label('NG_Hole_Size'),
        func.sum(DbHoledata.DBSnap).label('NG_DBSnap'),
        func.sum(DbHoledata.Recheck).label('Recheck'),
    ).filter(
        DbHoledata.Product==product
    ).group_by(
        DbHoledata.LOT
    ).order_by(
        func.max(DbHoledata.created_date).desc()
    ).all()


def prodlotresultperhour(db:Session, product:str, lot:str):
    return db.query(
        func.strftime("%Y-%m-%d %H:00:00", DbHoledata.created_date).label('Datetime'),
        (func.count(DbHoledata.id) - (func.sum(DbHoledata.HoleSlide)-func.sum(DbHoledata.HoleSlide)-func.sum(DbHoledata.DBSnap)-func.sum(DbHoledata.Recheck))).label('OK'),
        func.sum(DbHoledata.HoleSlide).label('NG_Hole_Slide'),
        func.sum(DbHoledata.HoleSize).label('NG_Hole_Size'),
        func.sum(DbHoledata.DBSnap).label('NG_DBSnap'),
        func.sum(DbHoledata.Recheck).label('Recheck'),
    ).filter(        
        DbHoledata.Product==product
    ).filter(
        DbHoledata.LOT==lot
    ).group_by(
        func.strftime("%Y-%m-%d %H:00:00", DbHoledata.created_date)
    ).all()

def prodlotresultperhour_gruopdate(db:Session, product:str, lot:str):
    return db.query(
        func.strftime("%Y-%m-%d", DbHoledata.created_date).label('Datetime'),
    ).filter(        
        DbHoledata.Product==product
    ).filter(
        DbHoledata.LOT==lot
    ).group_by(
        func.strftime("%Y-%m-%d", DbHoledata.created_date)
    ).all()


def prodlotresultpermin(db:Session, product:str, lot:str,Date:str, hour:str):
    return db.query(
        func.strftime("%Y-%m-%d %H:%M:00", DbHoledata.created_date).label('Datetime'),
        (func.count(DbHoledata.id) - (func.sum(DbHoledata.HoleSlide)-func.sum(DbHoledata.HoleSlide)-func.sum(DbHoledata.DBSnap)-func.sum(DbHoledata.Recheck))).label('OK'),
        func.sum(DbHoledata.HoleSlide).label('NG_Hole_Slide'),
        func.sum(DbHoledata.HoleSize).label('NG_Hole_Size'),
        func.sum(DbHoledata.DBSnap).label('NG_DBSnap'),
        func.sum(DbHoledata.Recheck).label('Recheck'),
    ).filter(        
        DbHoledata.Product==product
    ).filter(
        DbHoledata.LOT==lot
    ).filter(
        func.strftime("%Y-%m-%d", DbHoledata.created_date)==Date
    ).filter(
        func.strftime("%H", DbHoledata.created_date)==hour
    ).group_by(
        func.strftime("%Y-%m-%d %H:%M:00", DbHoledata.created_date)
    ).all()