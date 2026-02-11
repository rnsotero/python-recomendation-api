from sqlalchemy import Column, Integer, String
from app.database.database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    interesses = Column(String)
    historico_compras = Column(String)