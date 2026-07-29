while True:
    n, c, k = map(int, input().split())

    if n == c == k == 0:
        break

    frequencies = [0] * (k + 1)

    for _ in range(n):
        for number in map(int, input().split()):
            frequencies[number] += 1

    minimum = min(frequencies[1:])
    print(*[number for number in range(1, k + 1) if frequencies[number] == minimum])
