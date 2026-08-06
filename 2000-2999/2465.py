n = int(input())
i, j = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * n for _ in range(n)]
stack = [(i - 1, j - 1)]
visited[i - 1][j - 1] = True
count = 0

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

while stack:
    row, col = stack.pop()
    count += 1

    for dr, dc in directions:
        next_row = row + dr
        next_col = col + dc

        if 0 <= next_row < n and 0 <= next_col < n:
            if not visited[next_row][next_col] and grid[next_row][next_col] >= grid[row][col]:
                visited[next_row][next_col] = True
                stack.append((next_row, next_col))

print(count)
