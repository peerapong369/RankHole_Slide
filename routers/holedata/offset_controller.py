from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from sqlalchemy.sql import func
from datetime import datetime, timedelta

from models.holedata.offset_model import DbOffetData, OffsetBase


def create(db: Session, request: OffsetBase):
    new_offsetdata = DbOffetData(
        Product=request.Product,
        cal_lot=request.cal_lot,
        LA=request.LA,
        LB=request.LB,
        LC=request.LC,
        LD=request.LD,
        WA=request.WA,
        WB=request.WB,
        WC=request.WC,
        WD=request.WD,
        cal_pass = request.cal_pass
    )
    db.add(new_offsetdata)
    db.commit()
    db.refresh(new_offsetdata)
    return new_offsetdata


def delete(db: Session, id: int):
    offset = db.query(DbOffetData).filter(DbOffetData.id == id).first()
    db.delete(offset)
    db.commit()
    return JSONResponse(content={"detail": f"Calibration id {id} deleted"})


def read_offsetdata(db: Session):
    return db.query(DbOffetData).all()


def read_offset_last(db: Session, start: str, end: str):
    NOW = datetime.utcnow()
    return db.query(DbOffetData).filter(DbOffetData.created_date.between(start, end)).all()

 
def read_offsetdata_by_id(db: Session, id: int):
    return db.query(DbOffetData).filter(DbOffetData.id == id).first()

def offsetlot_group(db: Session):
    return db.query(
        DbOffetData
        ).group_by(
            DbOffetData.cal_lot
            ).order_by(
                DbOffetData.id.desc()
                ).all()


def offsetdataby_lot(db: Session, lot:str):
    return db.query(DbOffetData).filter(DbOffetData.cal_lot==lot).all()