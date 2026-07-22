N = int(input())

for _ in range(N):
    nome = input()
    notas = list(map(float ,input().split()))
    qtd_notas = len(notas)
    p1 = notas[0]
    if qtd_notas == 1:        
        media = (p1 + 0) / 2
    elif qtd_notas == 2:
        p2 = notas[1]
        media = (p1 + p2) / 2
    elif qtd_notas == 3:
        p2 = notas[1]
        p3 = notas[2]
        media = (p1 + p2 + p3) / 3
    else:
        p4 = notas.pop()
        menor_nota = min(notas)
        if p4 > menor_nota:
            indice_menor_nota = notas.index(menor_nota)
            notas[indice_menor_nota] = p4
        media = sum(notas) / 3
    print(f'{nome}: {media:.1f}')
