n, p = map(int, input().split())

black = set()
white = set()

for _ in range(p):
    black.add(tuple(map(int, input().split())))

for _ in range(p):
    white.add(tuple(map(int, input().split())))


def count_squares(blocked):
    previous = [0] * (n + 1)
    total = 0

    for row in range(1, n + 1):
        current = [0] * (n + 1)
        for column in range(1, n + 1):
            if (row, column) not in blocked:
                current[column] = 1 + min(
                    current[column - 1],
                    previous[column],
                    previous[column - 1],
                )
                total += current[column]
        previous = current

    return total


empty = count_squares(black | white)
black_areas = count_squares(white) - empty
white_areas = count_squares(black) - empty

print(black_areas, white_areas)
