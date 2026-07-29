n, m = map(int, input().split())

infinito = float('inf')
distancias = [[infinito] * n for _ in range(n)]

for i in range(n):
    distancias[i][i] = 0

for _ in range(m):
    u, v, w = map(int, input().split())
    if w < distancias[u][v]:
        distancias[u][v] = w
        distancias[v][u] = w

for k in range(n):
    for i in range(n):
        for j in range(n):
            nova_distancia = distancias[i][k] + distancias[k][j]
            if nova_distancia < distancias[i][j]:
                distancias[i][j] = nova_distancia

print(min(max(linha) for linha in distancias))
