from app.service import gerar_recomendacoes

class UsuarioFake:
    def __init__(self, interesses, historico_compras):
        self.interesses = interesses
        self.historico_compras = historico_compras
    
    def test_recomendacao_por_interesse():
        usuario = UsuarioFake(["games"], [])
        resultado = gerar_recomendacoes(usuario)
        assert "headset" in resultado

    def test_recomendacao_por_historico():
        usuario = UsuarioFake([], ["notebook"])
        resultado = gerar_recomendacoes(usuario)
        assert "mouse" in resultado    