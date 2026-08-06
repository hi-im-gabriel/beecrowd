from heapq import heappop, heappush

while True:
    try:
        line = input()
    except EOFError:
        break

    if not line.strip():
        continue

    n, m = map(int, line.split())
    graph = [[] for _ in range(n)]

    for _ in range(m):
        a, b, t, r = map(int, input().split())
        graph[a - 1].append((b - 1, t, r))

    inf = 10**30
    distances = [[inf] * n for _ in range(2)]
    heap = []

    for transport in range(2):
        distances[transport][0] = 0
        heappush(heap, (0, 0, transport))

    while heap:
        cost, city, transport = heappop(heap)

        if cost != distances[transport][city]:
            continue

        for destination, edge_transport, price in graph[city]:
            if edge_transport != transport:
                continue

            new_cost = cost + price
            if new_cost < distances[transport][destination]:
                distances[transport][destination] = new_cost
                heappush(heap, (new_cost, destination, transport))

    print(min(distances[0][n - 1], distances[1][n - 1]))
