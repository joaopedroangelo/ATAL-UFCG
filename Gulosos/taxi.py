def taxis(array):
    contador = 0
    quantidade_taxis = 0

    array.sort()
    i = 0
    while len(array) > 0:
        if contador + array[i] <= 4:
            contador += array[i]
            array.pop(i)
        elif contador + array[i] > 4:
            quantidade_taxis += 1
            contador = 0

    return quantidade_taxis            


def main():
    n = int(input())
    array = list(map(int, input().split()))
    print(taxis(array))


if __name__ == "__main__":
    main()