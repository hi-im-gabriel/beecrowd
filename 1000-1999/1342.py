while True:
    p, s = map(int, input().split())
    if p == 0 and s == 0:
        break

    traps = set(map(int, input().split()))
    n = int(input())
    positions = [0] * p
    blocked = [False] * p
    player = 0
    winner = 0

    for _ in range(n):
        d1, d2 = map(int, input().split())

        if winner:
            continue

        while blocked[player]:
            blocked[player] = False
            player = (player + 1) % p

        positions[player] += d1 + d2

        if positions[player] > s:
            winner = player + 1
        elif positions[player] in traps:
            blocked[player] = True

        player = (player + 1) % p

    print(winner)
