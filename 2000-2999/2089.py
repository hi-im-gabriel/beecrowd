while True:
    V, N = map(int, input().split())
    if V == 0 and N == 0:
        break

    moedas = list(map(int, input().split()))
    possibilidades = 1
    limite = (1 << (V + 1)) - 1

    for moeda in moedas:
        if moeda <= V:
            possibilidades |= possibilidades << moeda
            possibilidades &= limite

    if possibilidades & (1 << V):
        print("sim")
    else:
        print("nao")
