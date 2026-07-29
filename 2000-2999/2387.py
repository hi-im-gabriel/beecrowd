n = int(input())
consultas = []

for _ in range(n):
    inicio, fim = map(int, input().split())
    consultas.append((fim, inicio))

consultas.sort()

quantidade = 0
ultimo_fim = -1

for fim, inicio in consultas:
    if inicio >= ultimo_fim:
        quantidade += 1
        ultimo_fim = fim

print(quantidade)
