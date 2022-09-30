from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from sqlalchemy.sql import func
from datetime import datetime, timedelta

from models.machine.status_model import DbStatusData, StatusBase
from fastapi import HTTPException, status

def create(db: Session, request: StatusBase):
    new_status = DbStatusData(
        Status_str=request.Status_str,
        Status = request.Status,
        Product=request.Product,
        LOT=request.LOT,
    )
    db.add(new_status)
    db.commit()
    db.refresh(new_status)
    return new_status



def read_statusdata(db: Session):
    return db.query(DbStatusData).all()

 
def read_status_by_id(db: Session, id: int):
    return db.query(DbStatusData).filter(DbStatusData.id == id).first()

def update(db: Session, id: int, request: StatusBase):
    user = db.query(DbStatusData).filter(DbStatusData.id == id)
    if user.first() is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            default=f"User with id {id} not found"
        )
    else:
        user.update(
            {
                DbStatusData.Status_str: request.Status_str,
                DbStatusData.Status: request.Status,
                DbStatusData.Product: request.Product,
                DbStatusData.LOT: request.LOT,
            }
        )
        db.commit()
        return JSONResponse(
            content={"detail":f"User id {id} updated successful"},
            status_code=status.HTTP_200_OK
        )