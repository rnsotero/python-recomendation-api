from app.service import gerar_recomendacoes


class UsuarioFake:
    def __init__(self, interesses, historico_compras):
        self.interesses = interesses
        self.historico_compras = historico_compras


def test_deve_recomendar_com_base_em_interesse():
    usuario = UsuarioFake(["games"], [])
    resultado = gerar_recomendacoes(usuario)

    assert "headset" in resultado
    assert "cadeira gamer" in resultado


def test_deve_recomendar_com_base_no_historico():
    usuario = UsuarioFake([], ["notebook"])
    resultado = gerar_recomendacoes(usuario)

    assert "mouse" in resultado
    assert "suporte notebook" in resultado


def test_deve_priorizar_historico_sobre_interesses():
    usuario = UsuarioFake(["games"], ["notebook"])
    resultado = gerar_recomendacoes(usuario)

    assert "mouse" in resultado
    assert "headset" not in resultado  # garante prioridade


def test_nao_deve_retornar_recomendacoes_vazias_incorretas():
    usuario = UsuarioFake([], [])
    resultado = gerar_recomendacoes(usuario)

    assert isinstance(resultado, list)