from fastapi import FastAPI
from .modules import auth_router

app : FastAPI = FastAPI()

app.include_router(auth_router)