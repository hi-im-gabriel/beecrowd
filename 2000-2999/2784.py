from heapq import heappush, heappop

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v, ping = map(int, input().split())
    graph[u].append((v, ping))
    graph[v].append((u, ping))

server = int(input())
distances = [float('inf')] * (n + 1)
distances[server] = 0
queue = [(0, server)]

while queue:
    distance, island = heappop(queue)

    if distance != distances[island]:
        continue

    for neighbor, ping in graph[island]:
        new_distance = distance + ping

        if new_distance < distances[neighbor]:
            distances[neighbor] = new_distance
            heappush(queue, (new_distance, neighbor))

pings = [distances[island] for island in range(1, n + 1) if island != server]
print(max(pings) - min(pings))
