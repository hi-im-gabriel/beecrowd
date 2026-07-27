rank = {
    4: 0,
    5: 1,
    6: 2,
    7: 3,
    12: 4,
    11: 5,
    13: 6,
    1: 7,
    2: 8,
    3: 9,
}

n = int(input())
adalberto = 0

for _ in range(n):
    cards = list(map(int, input().split()))
    rounds = 0

    for i in range(3):
        if rank[cards[i]] >= rank[cards[i + 3]]:
            rounds += 1

    if rounds >= 2:
        adalberto += 1

print(adalberto, n - adalberto)
