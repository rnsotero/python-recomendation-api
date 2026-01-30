from fastapi import FastAPI
from .routes import router

app = FastAPI(title="API de recomendação de produtos")

app.include_router(router)
