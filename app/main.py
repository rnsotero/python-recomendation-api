from fastapi import FastAPI
from app.routes import router
from app.database.database import Base, engine

# Cria tabelas no banco
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Recommendation API")

app.include_router(router)