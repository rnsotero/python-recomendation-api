from fastapi import APIRouter
from app.models import Usuario
from app.service import gerar_recomendacoes

router = APIRouter()

@router.post("/recomendacoes")
def recomendar(usuario: Usuario):
    recomedacoes = gerar_recomendacoes(usuario)
    return {
        "usuario": usuario.nome,
        "total_recomendacoes": len(recomedacoes),
        "recomendacoes": recomedacoes
    }

