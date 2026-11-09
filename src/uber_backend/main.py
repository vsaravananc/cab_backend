from fastapi import FastAPI
from .modules import auth_router
from .database import Session_dp , create_database

app : FastAPI = FastAPI()


@app.on_event('startup')
def create_db():
    create_database()

app.include_router(auth_router)