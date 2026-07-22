N, L, D = map(int, input().split())

quantidade_necessaria = (N * D) / 1000
quantidade_minima = 0

while float(quantidade_minima) < quantidade_necessaria:
    quantidade_minima += L

print(quantidade_minima)
