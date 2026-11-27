# Não estamos criando novos arrays durante a divisão
# Estamos trabalhando sobre o mesmo array original e delimitando os subarrays pelos índices

# A execução recursiva ocorre em profundidade.
# Ou seja, o algoritmo não divide todas as metades simultaneamente, nível por nível.
# Ele explora primeiro o ramo esquerdo, depois o direito.

# Além disso, o merge começa a ser executado conforme as chamadas recursivas retornam
# Não apenas depois que toda árvore foi dividida

def mergeSort(array, left, right):
    if left < right:
        mediana = (left + right) // 2 
        mergeSort(array, left, mediana)
        mergeSort(array, mediana + 1, right)
        merge(array, left, mediana, right)


def merge(array, left, mediana, right):
    # Obtemos os tamanhos dos subarrays
    tamanho_esquerda = mediana - left + 1
    tamanho_direita = right - mediana

    # Cria os arrays auxiliares
    esquerda = []
    direita = []

    # Insere os elementos nos arrays auxiliares
    # Agora sim estamos manipulando novos arrays
    # Não é apenas divisão por índices, como era no MergeSort
    for i in range(tamanho_esquerda):
        esquerda.append(array[left + i])

    for j in range(tamanho_direita):
        direita.append(array[mediana + 1 + j])

    # Adicionamos sentinelas para marcar os fins dos arrays
    # Quando todos os elementos de um dos subarrays forem consumidos, seu ponteiro estará no infinito
    # Como qualquer inteiro é menor, os elementos restantes do outro subarray serão selecionados
    esquerda.append(float('inf'))
    direita.append(float('inf'))

    indice_esquerda = 0
    indice_direita = 0

    for k in range(left, right + 1):
        if esquerda[indice_esquerda] <= direita[indice_direita]:
            array[k] = esquerda[indice_esquerda]
            indice_esquerda += 1
        else:
            array[k] = direita[indice_direita]
            indice_direita += 1


print(mergeSort([8, 3, 5, 1, 7, 2, 6, 4], 0, 8))