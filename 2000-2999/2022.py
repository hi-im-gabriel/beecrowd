while True:
    try:
        linha = input().strip()
        while not linha:
            linha = input().strip()
    except EOFError:
        break

    dono, quantidade = linha.split()
    presentes = []

    for _ in range(int(quantidade)):
        objeto = input().strip()
        preco, preferencia = input().split()
        presentes.append((objeto, float(preco), int(preferencia)))

    presentes.sort(key=lambda presente: (-presente[2], presente[1], presente[0]))

    print(f"Lista de {dono}")
    for objeto, preco, _ in presentes:
        print(f"{objeto} - R${preco:.2f}")
    print()
