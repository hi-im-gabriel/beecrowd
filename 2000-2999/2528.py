from collections import deque


while True:
    try:
        n, m = map(int, input().split())
    except EOFError:
        break

    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    c, r, e = map(int, input().split())
    distances = [-1] * (n + 1)
    distances[c] = 0
    queue = deque([c])

    while queue:
        city = queue.popleft()

        if city == r:
            break

        for neighbor in graph[city]:
            if neighbor != e and distances[neighbor] == -1:
                distances[neighbor] = distances[city] + 1
                queue.append(neighbor)

    print(distances[r])
