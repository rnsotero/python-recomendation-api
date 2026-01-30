def gerar_recomendacoes(usuario):
    base_recomendacoes = {
        "tecnologia": ["teclado mecânico", "monitor", "mouse gamer"],
        "games": ["controle", "headset", "cadeira gamer"],
        "livros": ["kindle", "luminária de leitura"]
    }

    recomendacoes = []

    for interesse in usuario.interesses:
        if interesse in base_recomendacoes:
            recomendacoes.extend(base_recomendacoes[interesse])

    return list(set(recomendacoes))
