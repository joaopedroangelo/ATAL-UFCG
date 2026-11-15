def permutacao(aux, array, i, resultado):
    if (i == len(array)):
        resultado.append(aux.copy())
        return

    for j in range(len(array)):
        if isValid(array[j], aux, i):
            aux[i] = array[j]
            permutacao(aux, array, i + 1, resultado)


def isValid(num, aux, i):
    for j in range(i):
        if aux[j] == num:
            return False
    return True


A = [1, 2, 3]
aux = [0] * len(A)
resultado = []
permutacao(aux, A, 0, resultado)
print(resultado)
