c = int(input())

for caso in range(1, c + 1):
    m, n, x, y = map(int, input().split())
    parede = [list(map(int, input().split())) for _ in range(m)]

    print(f"Parede {caso}:")
    for i in range(m):
        linha = []
        for j in range(n):
            distancia = max(abs(i - (x - 1)), abs(j - (y - 1)))
            aumento = max(1, 10 - distancia)
            linha.append(parede[i][j] + aumento)
        print(*linha)
