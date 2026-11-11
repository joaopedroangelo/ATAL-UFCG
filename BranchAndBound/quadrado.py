def quadrado(n):
    soma = 0
    for i in range(0, len(n)):
        soma += n[i]

    return "true" if soma % 4 == 0 else "false"


def main():
    length = int(input())
    n = list(map(int, input().split()))
    print(quadrado(n))


if __name__ == "__main__":
    main()