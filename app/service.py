def gerar_recomendacoes(usuario):
    base = usuario.historico_compras
    if usuario.historico_compras:
        base = usuario.historico_compras
    else:
        base = usuario.interesses
 
    recomendacoes = []

    for item in base:
        item = item.lower()

        if item == "tecnologia":
            recomendacoes.extend(["teclado mecãnico", "monitor"])
        if item == "games":
            recomendacoes.extend(["cadeira gamer", "headset"])
        if item == "notebook":
            recomendacoes.extend(["mouse","suporte notebook"])    

    return list(set(recomendacoes))
