n, m = map(int, input().split())
stones = [0] * n

for _ in range(m):
    position, distance = map(int, input().split())

    for stone in range(position - 1, n, distance):
        stones[stone] = 1

    for stone in range(position - 1, -1, -distance):
        stones[stone] = 1

for stone in stones:
    print(stone)
