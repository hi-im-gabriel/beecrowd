teste = 1

while True:
    n = int(input())

    if n == -1:
        break

    pedacos = (2 ** n + 1) ** 2

    print(f"Teste {teste}")
    print(pedacos)
    print()

    teste += 1
