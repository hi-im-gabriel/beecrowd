from collections import deque


def add_edge(graph, u, v, capacity):
    graph[u].append([v, capacity, len(graph[v])])
    graph[v].append([u, 0, len(graph[u]) - 1])


def maximum_flow(graph, source, sink):
    total = 0

    while True:
        level = [-1] * len(graph)
        level[source] = 0
        queue = deque([source])

        while queue:
            u = queue.popleft()
            for v, capacity, reverse in graph[u]:
                if capacity > 0 and level[v] == -1:
                    level[v] = level[u] + 1
                    queue.append(v)

        if level[sink] == -1:
            return total

        position = [0] * len(graph)

        def send_flow(u, flow):
            if u == sink:
                return flow

            while position[u] < len(graph[u]):
                edge = graph[u][position[u]]
                v, capacity, reverse = edge

                if capacity > 0 and level[v] == level[u] + 1:
                    sent = send_flow(v, min(flow, capacity))
                    if sent:
                        edge[1] -= sent
                        graph[v][reverse][1] += sent
                        return sent

                position[u] += 1

            return 0

        while True:
            sent = send_flow(source, 10 ** 9)
            if sent == 0:
                break
            total += sent


instance = 1

while True:
    try:
        line = input()
        while not line.strip():
            line = input()
    except EOFError:
        break

    n, m, k = map(int, line.split())
    capacities = list(map(int, input().split()))

    source = 0
    horse_start = 1
    soldier_start = horse_start + n
    sink = soldier_start + m
    graph = [[] for _ in range(sink + 1)]

    for horse in range(n):
        add_edge(graph, source, horse_start + horse, capacities[horse])

    for soldier in range(m):
        add_edge(graph, soldier_start + soldier, sink, 1)

    affinities = set()
    for _ in range(k):
        horse, soldier = map(int, input().split())
        affinities.add((horse - 1, soldier - 1))

    for horse, soldier in affinities:
        add_edge(graph, horse_start + horse, soldier_start + soldier, 1)

    answer = maximum_flow(graph, source, sink)
    print(f"Instancia {instance}")
    print(answer)
    print()
    instance += 1
