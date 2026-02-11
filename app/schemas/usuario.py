from pydantic import BaseModel
from typing import List, Optional

class UsuarioCreate(BaseModel):
    nome: str
    interesses: List[str]
    historico_compras: Optional[List[str]] = []