def gerar_recomendacoes(usuario):

    base = usuario.historico_compras if usuario.historico_compras else usuario.interesses

    recomendacoes = []

    for item in base:
        item = item.lower().strip()

        if item == "tecnologia":
            recomendacoes.extend(["teclado mecânico", "monitor"])

        elif item == "games":
            recomendacoes.extend(["cadeira gamer", "headset"])

        elif item == "notebook":
            recomendacoes.extend(["mouse", "suporte notebook"])

    return list(set(recomendacoes))