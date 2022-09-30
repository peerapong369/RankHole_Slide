from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from models.database import get_db
from models.users.users_model import UserBase, UserDisplayBase

from typing import List

from models.users.users_model import UserBase
from routers.users import user_controller

#from utils.oauth2 import access_user_token

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/", response_model=List[UserDisplayBase])
def get_all_user(db:Session = Depends(get_db)):
    return user_controller.read_users(db)


@router.get("/{id}", response_model=UserDisplayBase)
def user_by_id(id: int, db:Session=Depends(get_db)):
    return user_controller.read_user_by_id(db, id)


@router.post("/")
def register_user(request:UserBase, db:Session=Depends(get_db)):
    return user_controller.create(db, request)


@router.put("/{id}")
def put_api(id: int, request:UserBase, db:Session=Depends(get_db)):
    return user_controller.update(db, id, request)

@router.delete("/{id}")
def delete_api(id: int, db:Session=Depends(get_db)):
    return user_controller.delete(db, id)

