from curses.ascii import NUL
from email.policy import default
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse

from models.users.users_model import DbUser, UserBase
from utils.hash import Hash

from fastapi import HTTPException, status

def create(db: Session, request: UserBase):
    new_user = DbUser(
        username = request.username,
        password = Hash.bcrypt(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def read_users(db: Session):
    return db.query(DbUser).all()

def read_user_by_id(db: Session, id: int):
    return db.query(DbUser).filter(DbUser.id == id).first()


def delete(db: Session, id: int):
    user = db.query(DbUser).filter(DbUser.id == id).first()
    db.delete(user)
    db.commit()
    return JSONResponse(content={"detail": f"User id {id} deleted"})


def update(db: Session, id: int, request: UserBase):
    user = db.query(DbUser).filter(DbUser.id == id)
    if user.first() is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            default=f"User with id {id} not found"
        )
    else:
        user.update(
            {
                DbUser.username: request.username,
                DbUser.password: Hash.bcrypt(request.password)
            }
        )
        db.commit()
        return JSONResponse(
            content={"detail":f"User id {id} updated successful"},
            status_code=status.HTTP_200_OK
        )

