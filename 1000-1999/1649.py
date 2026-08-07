while True:
    n, m, r, c = map(int, input().split())

    if n == 0 and m == 0 and r == 0 and c == 0:
        break

    painting = [input() for _ in range(n)]
    changes = [[0] * (m + 1) for _ in range(n + 1)]
    operations = 0
    possible = True

    for i in range(n):
        for j in range(m):
            current = changes[i][j]

            if i > 0:
                current ^= changes[i - 1][j]
            if j > 0:
                current ^= changes[i][j - 1]
            if i > 0 and j > 0:
                current ^= changes[i - 1][j - 1]

            target = int(painting[i][j])

            if current != target:
                if i + r > n or j + c > m:
                    possible = False
                else:
                    current ^= 1
                    operations += 1
                    changes[i + r][j] ^= 1
                    changes[i][j + c] ^= 1
                    changes[i + r][j + c] ^= 1

            changes[i][j] = current

    print(operations if possible else -1)
