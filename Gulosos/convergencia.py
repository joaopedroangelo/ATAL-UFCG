def guloso_convergencia(amigos):
    amigos = sorted(amigos)
    T = amigos[len(amigos) // 2]  #mediana

    esq = [x for x in amigos if x < T]      # candidatos à esquerda de T
    dir = [x for x in amigos if x > T]      # candidatos à direita de T

    chamadas = 0
    while len(esq) > 0 or len(dir) > 0:
        if len(esq) > 0 and len(dir) > 0:
            # Caso 1: há gente dos DOIS lados.
            # Uma chamada leva um da esquerda e um da direita até T.
            esq.pop()
            dir.pop()
        elif len(esq) > 0 and len(dir) == 0:
            # Caso 2: só sobrou gente à ESQUERDA.
            # A chamada é feita com alguém já em T: resolve apenas 1.
            esq.pop()
        elif len(esq) == 0 and len(dir) > 0:
            # Caso 3: só sobrou gente à DIREITA.
            # A chamada é feita com alguém já em T: resolve apenas 1.
            dir.pop()
        chamadas += 1   # cada passo do laço = 1 chamada
    return chamadas


def main():
    numero_de_casos_de_teste = int(input())
    for _ in range(numero_de_casos_de_teste):
        numero_de_candidatos = int(input())
        candidatos = list(map(int, input().split()))
        resultado = guloso_convergencia(candidatos)
        print(resultado)


if __name__ == "__main__":
    main()