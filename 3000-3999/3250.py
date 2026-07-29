from collections import deque

f, s, g, u, d = map(int, input().split())

visited = bytearray(f + 1)
visited[s] = 1
queue = deque([s])
presses = 0

while queue:
    for _ in range(len(queue)):
        floor = queue.popleft()

        if floor == g:
            print(presses)
            raise SystemExit

        up = floor + u
        if up <= f and not visited[up]:
            visited[up] = 1
            queue.append(up)

        down = floor - d
        if down >= 1 and not visited[down]:
            visited[down] = 1
            queue.append(down)

    presses += 1

print("use the stairs")
