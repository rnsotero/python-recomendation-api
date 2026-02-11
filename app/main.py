from fastapi import FastAPI
from app.database.database import Base, engine
from app.database.models import Base
from app.routes import router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(router)