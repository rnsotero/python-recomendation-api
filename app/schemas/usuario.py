from pydantic import BaseModel, Field
from typing import List, Optional

class UsuarioCreate(BaseModel):
    nome: str = Field(..., min_length=2, example="Renato")
    interesses: List[str] = Field(..., min_items=1)
    historico_compras: Optional[List[str]] = []