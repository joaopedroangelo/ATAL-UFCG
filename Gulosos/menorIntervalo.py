def guloso(k, array):
    solucao = []
    while len(array) > 0:
        if array[0] <= k:
            solucao.append(array[0] + k) 
            array.pop(0)
        elif array[0] > k:
            solucao.append(array[0] - k)
            array.pop(0)
    return max(solucao) - min(solucao)


def main():
    length_array, k = map(int, input().split())
    array = list(map(int, input().split()))
    print(guloso(k, array))


if __name__ == "__main__":
    main()
