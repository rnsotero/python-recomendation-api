from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import logging

from app.database.deps import get_db
from app.database.models import Usuario
from app.schemas.usuario import UsuarioCreate
from app.service import gerar_recomendacoes

# Configuração de log
logging.basicConfig(level=logging.INFO)

router = APIRouter(
    prefix="/api",
    tags=["Recomendação"]
)

# 🔥 ROTA ROOT (boa prática)
@router.get("/")
def root():
    return {"message": "Recommendation API running 🚀"}

# 🔥 HEALTH CHECK (nível produção)
@router.get("/health")
def health():
    return {"status": "ok"}

# 🔥 ROTA PRINCIPAL
@router.post("/recomendar")
def recomendar(usuario: UsuarioCreate, db: Session = Depends(get_db)):

    # Salvar usuário no banco
    novo_usuario = Usuario(
        nome=usuario.nome,
        interesses=",".join(usuario.interesses),
        historico_compras=",".join(usuario.historico_compras or [])
    )

    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)

    # Gerar recomendações
    recomendacoes = gerar_recomendacoes(usuario)

    # Log (diferencial profissional)
    logging.info(f"Usuário {usuario.nome} recebeu recomendações")

    # Resposta padrão de API
    return {
        "success": True,
        "data": {
            "id": novo_usuario.id,
            "usuario": usuario.nome,
            "recomendacoes": recomendacoes
        }
    }