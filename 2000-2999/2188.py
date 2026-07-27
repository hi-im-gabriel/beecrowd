teste = 1

while True:
    n = int(input())

    if n == 0:
        break

    x, y, u, v = map(int, input().split())

    for _ in range(n - 1):
        novo_x, novo_y, novo_u, novo_v = map(int, input().split())
        x = max(x, novo_x)
        y = min(y, novo_y)
        u = min(u, novo_u)
        v = max(v, novo_v)

    print(f"Teste {teste}")

    if x < u and v < y:
        print(x, y, u, v)
    else:
        print("nenhum")

    print()
    teste += 1
