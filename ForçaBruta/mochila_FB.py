def gerar_combinacoes(pesos):
    combinacoes = [[]]

    for peso in pesos:
        novas_combinacoes = []
        for combinacao in combinacoes:
            novas_combinacoes.append(combinacao + [peso])
        combinacoes += novas_combinacoes

    return combinacoes


def calcular_peso_valor(combinacao, pesos, valores):
    peso_total = 0
    valor_total = 0

    for peso in combinacao:
        i = pesos.index(peso)
        peso_total += peso
        valor_total += valores[i]

    return peso_total, valor_total


def mochila_forca_bruta(pesos, valores, capacidade):
    combinacoes = gerar_combinacoes(pesos)
    melhor_valor = 0

    for combinacao in combinacoes:
        peso, valor = calcular_peso_valor(combinacao, pesos, valores)
        if peso <= capacidade:
            melhor_valor = max(melhor_valor, valor)

    return melhor_valor
