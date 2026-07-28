n = int(input())

roads = [[] for _ in range(n)]
reverse_roads = [[] for _ in range(n)]

for _ in range(n):
    a, b = map(int, input().split())
    roads[a - 1].append(b - 1)
    reverse_roads[b - 1].append(a - 1)


def reaches_all(graph):
    visited = [False] * n
    visited[0] = True
    stack = [0]
    count = 1

    while stack:
        city = stack.pop()
        for next_city in graph[city]:
            if not visited[next_city]:
                visited[next_city] = True
                count += 1
                stack.append(next_city)

    return count == n


print("S" if reaches_all(roads) and reaches_all(reverse_roads) else "N")
