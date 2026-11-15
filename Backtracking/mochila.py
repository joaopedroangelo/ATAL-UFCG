def backtracking(pesos, valores, capacidade, i, valor_atual):

    if isSolution(pesos, i):
        return valor_atual
    
    # Decisão 1: não colocar o item
    sem_item = backtracking(
        pesos, valores, capacidade, i + 1, valor_atual
    )

    # Decisão 2: colocar o item
    com_item = 0
    if isValid(pesos[i], capacidade):
        com_item = backtracking(
            pesos,
            valores,
            capacidade - pesos[i],
            i + 1,
            valor_atual + valores[i]
        )

    return max(sem_item, com_item)


def isSolution(pesos, i):
    return i == len(pesos)


def isValid(peso, capacidade):
    return peso <= capacidade


print("Backtracking - Mochila")
pesos = [2, 3, 4, 5]
valores = [3, 4, 5, 6]
capacidade = 5
resultado = backtracking(pesos, valores, capacidade, 0, 0)
print("Resultado:", resultado)