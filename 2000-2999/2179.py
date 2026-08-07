values = []
while len(values) < 3:
    values.extend(map(int, input().split()))

n, row, col = values
path = [row * n + col + 1]
total = 1

moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
direction = 0
steps = 1

while len(path) < n * n:
    for _ in range(2):
        dr, dc = moves[direction]

        for _ in range(steps):
            row += dr
            col += dc
            total += 1

            if 0 <= row < n and 0 <= col < n:
                path.append(row * n + col + 1)
                if len(path) == n * n:
                    break

        if len(path) == n * n:
            break

        direction = (direction + 1) % 4

    steps += 1

print(*path)
print(total)
