L, C = map(int, input().split())
A, B = map(int, input().split())

floor = [list(map(int, input().split())) for _ in range(L)]

row = A - 1
column = B - 1

while True:
    floor[row][column] = 0

    if row > 0 and floor[row - 1][column] == 1:
        row -= 1
    elif row + 1 < L and floor[row + 1][column] == 1:
        row += 1
    elif column > 0 and floor[row][column - 1] == 1:
        column -= 1
    elif column + 1 < C and floor[row][column + 1] == 1:
        column += 1
    else:
        break

print(row + 1, column + 1)
