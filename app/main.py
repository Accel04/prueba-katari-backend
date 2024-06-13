from fastapi import FastAPI
from .routers import users, companies
from .database import engine, SessionLocal
from . import models, schemas, crud

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)
app.include_router(companies.router)