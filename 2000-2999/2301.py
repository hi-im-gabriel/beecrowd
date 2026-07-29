teste = 1

while True:
    p, r = map(int, input().split())

    if p == 0 and r == 0:
        break

    participantes = list(map(int, input().split()))

    for _ in range(r):
        rodada = list(map(int, input().split()))
        n, ordem = rodada[0], rodada[1]
        acoes = rodada[2:]
        participantes = [participantes[i] for i in range(n) if acoes[i] == ordem]

    print(f"Teste {teste}")
    print(participantes[0])
    print()
    teste += 1
