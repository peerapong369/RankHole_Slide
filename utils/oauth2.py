from base64 import encode
from datetime import timedelta, datetime
from os import stat
from typing import Optional

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from jose import JWTError, jwt
from decouple import config


SECRET_KEY = config("SECRET_KEY")
ALGORITHM = config("ALGORITHM")

oauth2_schema = OAuth2PasswordBearer(tokenUrl="token")

def create_access_token(data:dict, expire_delta:Optional[timedelta]=None):
    to_encode = data.copy()
    expire = generate_expire_date(expire_delta)
    to_encode.update({"exp":expire})
    encode_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encode_jwt

def generate_expire_date(expire_delta:Optional[timedelta]=None):
    if expire_delta:
        expire = datetime.utcnow() + expire_delta
    else:
        expire = datetime.utcnow() + timedelta(days=1)
    return expire


def access_user_token(token:str = Depends(oauth2_schema)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username:str = payload.get("sub")
        if username is None:
            pass
    except JWTError:
        pass


def credentials_exception():
    return HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not  validate credentials"
    )