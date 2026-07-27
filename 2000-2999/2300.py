teste = 1

while True:
    e, l = map(int, input().split())

    if e == 0 and l == 0:
        break

    pai = list(range(e + 1))

    def encontrar(x):
        while pai[x] != x:
            pai[x] = pai[pai[x]]
            x = pai[x]
        return x

    for _ in range(l):
        x, y = map(int, input().split())
        raiz_x = encontrar(x)
        raiz_y = encontrar(y)

        if raiz_x != raiz_y:
            pai[raiz_x] = raiz_y

    raiz = encontrar(1)
    normal = all(encontrar(estacao) == raiz for estacao in range(2, e + 1))

    print(f"Teste {teste}")
    print("normal" if normal else "falha")
    print()

    teste += 1
