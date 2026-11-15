def N_Rainhas(tabuleiro, linha, N, resultado):
    if linha == N:
        resultado.append(tabuleiro[:])
        return

    for coluna in range(N):
        if is_safe(tabuleiro, linha, coluna, N):
            tabuleiro[linha] = coluna + 1
            N_Rainhas(tabuleiro, linha + 1, N, resultado)
            tabuleiro[linha] = 0


def is_safe(tabuleiro, linha, coluna, N):
    for i in range(linha):
        if (tabuleiro[i] == coluna + 1) or (abs(tabuleiro[i] - (coluna + 1)) == abs(i - linha)):
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