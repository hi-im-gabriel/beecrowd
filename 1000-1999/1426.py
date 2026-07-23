n = int(input())

for _ in range(n):
    v = [[0] * 11 for _ in range(11)]

    for i in range(1, 10, 2):
        values = list(map(int, input().split()))
        for j, val in zip(range(1, i + 1, 2), values):
            v[i][j] = val

    for i in range(1, 8, 2):
        v[9][i + 1] = (v[7][i] - v[9][i] - v[9][i + 2]) // 2

    for i in range(8, 0, -1):
        for j in range(1, i + 1):
            v[i][j] = v[i + 1][j] + v[i + 1][j + 1]

    for i in range(1, 10):
        print(' '.join(str(v[i][j]) for j in range(1, i + 1)))
