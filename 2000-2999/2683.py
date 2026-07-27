from array import array


n = int(input())
galerias = [array("I") for _ in range(201)]

for _ in range(n):
    u, v, w = map(int, input().split())
    galerias[w].append((u << 10) | v)


def custo(ordem):
    pai = list(range(1001))
    tamanho = [1] * 1001
    total = 0

    def encontrar(x):
        while pai[x] != x:
            pai[x] = pai[pai[x]]
            x = pai[x]
        return x

    for peso in ordem:
        for galeria in galerias[peso]:
            u = galeria >> 10
            v = galeria & 1023
            raiz_u = encontrar(u)
            raiz_v = encontrar(v)

            if raiz_u != raiz_v:
                if tamanho[raiz_u] < tamanho[raiz_v]:
                    raiz_u, raiz_v = raiz_v, raiz_u
                pai[raiz_v] = raiz_u
                tamanho[raiz_u] += tamanho[raiz_v]
                total += peso

    return total


print(custo(range(200, 0, -1)))
print(custo(range(1, 201)))
