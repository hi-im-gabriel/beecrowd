def read_values():
    while True:
        line = input().split()
        if line:
            return map(int, line)


while True:
    try:
        n, m = read_values()
    except EOFError:
        break

    black = [tuple(read_values()) for _ in range(n)]
    white = [tuple(read_values()) for _ in range(m)]

    left = [[0] * n for _ in range(n)]

    for i in range(n - 1):
        xi, yi = black[i]
        row = left[i]

        for j in range(i + 1, n):
            xj, yj = black[j]
            dx = xj - xi
            dy = yj - yi
            mask = 0
            bit = 1

            for x, y in white:
                if dx * (y - yi) > dy * (x - xi):
                    mask |= bit
                bit <<= 1

            row[j] = mask

    answer = 0

    for i in range(n - 2):
        row_i = left[i]

        for j in range(i + 1, n - 1):
            first = row_i[j]
            row_j = left[j]

            for k in range(j + 1, n):
                second = row_j[k]
                inside = ~(first ^ second) & (second ^ row_i[k])
                count = inside.bit_count()
                answer += count * count

    print(answer)
