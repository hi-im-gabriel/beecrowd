h, l = map(int, input().split())
mosaic = [list(map(int, input().split())) for _ in range(h)]
visited = [[False] * l for _ in range(h)]
answer = h * l

for start_row in range(h):
    for start_column in range(l):
        if visited[start_row][start_column]:
            continue

        color = mosaic[start_row][start_column]
        stack = [(start_row, start_column)]
        visited[start_row][start_column] = True
        area = 0

        while stack:
            row, column = stack.pop()
            area += 1

            if row > 0 and not visited[row - 1][column] and mosaic[row - 1][column] == color:
                visited[row - 1][column] = True
                stack.append((row - 1, column))
            if row + 1 < h and not visited[row + 1][column] and mosaic[row + 1][column] == color:
                visited[row + 1][column] = True
                stack.append((row + 1, column))
            if column > 0 and not visited[row][column - 1] and mosaic[row][column - 1] == color:
                visited[row][column - 1] = True
                stack.append((row, column - 1))
            if column + 1 < l and not visited[row][column + 1] and mosaic[row][column + 1] == color:
                visited[row][column + 1] = True
                stack.append((row, column + 1))

        answer = min(answer, area)

print(answer)
