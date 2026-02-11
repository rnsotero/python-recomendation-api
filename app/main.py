from fastapi import FastAPI
from .database.database import Base, engine
from .database.models import Base
from .routes import router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router)