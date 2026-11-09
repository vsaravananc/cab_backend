from sqlmodel import SQLModel , create_engine , Session
from uber_backend.modules.auth.schema import User
from typing import Annotated 
from fastapi import Depends

DB_FILE_NAME = 'uber.db'
DB_URL = f'sqlite:///{DB_FILE_NAME}'
ENGINE = create_engine(DB_URL,connect_args={'check_same_thread':False})

def create_database():
    SQLModel.metadata.create_all(ENGINE)

def session_dp ():
    with Session(ENGINE) as session:
        yield session

Session_dp = Annotated[Session , Depends(session_dp)]