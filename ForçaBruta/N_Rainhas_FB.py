def N_Rainhas(tabuleiro, linha, N, resultado):
    if linha == N:
        if is_valid(tabuleiro):
            resultado.append(tabuleiro[:])
        return resultado

    for coluna in range(N):
        tabuleiro[linha] = coluna + 1
        N_Rainhas(tabuleiro, linha + 1, N, resultado)
        tabuleiro[linha] = 0


def is_valid(tabuleiro):
    for linha in range(0, len(tabuleiro)):
        for coluna in range(linha + 1, len(tabuleiro)):
            if tabuleiro[linha] == tabuleiro[coluna] or abs(tabuleiro[linha] - tabuleiro[coluna]) == abs(linha - coluna):
                return False
    return True


print("Digite o número de rainhas (N):")
N = int(input())
tabuleiro = [0] * N
resultado = []
N_Rainhas(tabuleiro, 0, N, resultado)
print(f"Total de soluções para {N} rainhas: {len(resultado)}")
print("Soluções encontradas:")
for solucao in resultado:
    print(solucao)