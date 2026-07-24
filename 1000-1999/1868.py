while True:
    n = int(input())
    if n == 0:
        break

    row = n // 2
    column = n // 2
    directions = ((0, 1), (-1, 0), (0, -1), (1, 0))
    positions = [(row, column)]
    direction = 0
    step_size = 1

    while len(positions) < n * n:
        for _ in range(2):
            for _ in range(step_size):
                if len(positions) == n * n:
                    break
                row += directions[direction][0]
                column += directions[direction][1]
                positions.append((row, column))
            direction = (direction + 1) % 4
        step_size += 1

    for row, column in positions:
        lines = ["O" * n for _ in range(n)]
        lines[row] = lines[row][:column] + "X" + lines[row][column + 1:]
        for line in lines:
            print(line)
        print("@")
