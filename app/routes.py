from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .database.deps import get_db
from .database.models import Usuario
from .schemas import UsuarioCreate
from .service import gerar_recomendacoes

router = APIRouter()

@router.post("/recomendar")
def recomendar(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    novo_usuario = Usuario(
        nome=usuario.nome,
        interesses=",".join(usuario.interesses),
        historico_compras=",".join(usuario.historico_compras or [])
    )

    db.add(novo_usuario)
    db.commit()

    return gerar_recomendacoes(usuario)
