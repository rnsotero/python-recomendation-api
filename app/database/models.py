from sqlalchemy import Column, Integer, String
from app.database.database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    interesses = Column(String(255), nullable=False)
    historico_compras = Column(String(255), nullable=True)