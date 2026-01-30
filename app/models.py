from pydantic import BaseModel
from typing import List

class Produto(BaseModel):
    id: int
    nome: str
    categoria: str

class Usuario(BaseModel):
    id: int
    nome: str
    interesses: List[str]
