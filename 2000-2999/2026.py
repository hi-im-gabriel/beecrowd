g = int(input())

for caso in range(1, g + 1):
    p = int(input())
    w = int(input())
    dp = [0] * (w + 1)

    for _ in range(p):
        enfeites, peso = map(int, input().split())
        for capacidade in range(w, peso - 1, -1):
            dp[capacidade] = max(dp[capacidade], dp[capacidade - peso] + enfeites)

    print(f"Galho {caso}:")
    print(f"Numero total de enfeites: {dp[w]}")
    print()
