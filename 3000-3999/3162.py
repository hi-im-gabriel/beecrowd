from math import dist

lista = [list(map(int, input().split())) for _ in range(int(input()))]

for i, el in enumerate(lista):
    ndist = 9999
    for j, _ in enumerate(lista):
        if i == j:
            continue
        if dist(el, lista[j]) < ndist:
            ndist = dist(el, lista[j])
            
    if ndist <= 20:
        print('A')
    elif ndist > 20 and ndist <= 50:
        print('M')
    else:
        print('B')
