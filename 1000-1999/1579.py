casos = int(input())

for _ in range(casos):
    n_paineis, caminhoes, frete = map(int, input().split())
    pesos = list(map(int, input().split()))

    menor = max(pesos)
    maior = sum(pesos)

    while menor < maior:
        capacidade = (menor + maior) // 2
        usados = 1
        carga = 0

        for peso in pesos:
            if carga + peso > capacidade:
                usados += 1
                carga = peso
            else:
                carga += peso

        if usados <= caminhoes:
            maior = capacidade
        else:
            menor = capacidade + 1

    print(f"{menor} ${menor * caminhoes * frete}")
