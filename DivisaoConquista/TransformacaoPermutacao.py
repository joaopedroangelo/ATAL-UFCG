def profundidades(array, left, right, profundidade, resultado):
    indice_max = array.index(max(array))

    if (left == indice_max and right == indice_max):
        return resultado

    resultado[indice_max] = profundidade
    profundidades(array, left, indice_max - 1, profundidade + 1, resultado)
    profundidades(array, indice_max, right, profundidade + 1, resultado)


array = [3, 5, 2, 1, 4]
resultado = [0] * len(array)
print(profundidades(array, 0, len(array) - 1, 0, resultado))