from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from sqlalchemy.sql import func
from datetime import datetime, timedelta

from models.holedata.calibration_model import DbCalibrationHoleData, CalibrationBase


def create(db: Session, request: CalibrationBase):
    new_calibtationdata = DbCalibrationHoleData(
        Product=request.Product,
        LOT=request.LOT,
        sheet=request.sheet,
        round=request.round,
        LA=request.LA,
        LB=request.LB,
        LC=request.LC,
        LD=request.LD,
        WA=request.WA,
        WB=request.WB,
        WC=request.WC,
        WD=request.WD,
    )
    db.add(new_calibtationdata)
    db.commit()
    db.refresh(new_calibtationdata)
    return new_calibtationdata


def delete(db: Session, id: int):
    cal = db.query(DbCalibrationHoleData).filter(DbCalibrationHoleData.id == id).first()
    db.delete(cal)
    db.commit()
    return JSONResponse(content={"detail": f"Calibration id {id} deleted"})


def read_calibrationdata(db: Session):
    return db.query(DbCalibrationHoleData).all()


def read_calibrationdata_last(db: Session, start: str, end: str):
    NOW = datetime.utcnow()
    return db.query(DbCalibrationHoleData).filter(DbCalibrationHoleData.created_date.between(start, end)).all()

 
def read_calibrationdata_by_id(db: Session, id: int):
    return db.query(DbCalibrationHoleData).filter(DbCalibrationHoleData.id == id).first()

def callot_group(db: Session):
    return db.query(
        DbCalibrationHoleData
        ).group_by(
            DbCalibrationHoleData.LOT
            ).order_by(
                DbCalibrationHoleData.id.desc()
                ).all()


def caldataby_lot(db: Session, lot:str):
    return db.query(DbCalibrationHoleData).filter(DbCalibrationHoleData.LOT==lot).all()