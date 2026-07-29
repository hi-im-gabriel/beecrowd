from heapq import heappush, heappop

instance = 1

while True:
    try:
        line = input()
        while not line.strip():
            line = input()
    except EOFError:
        break

    n, m = map(int, line.split())
    routes = []

    for _ in range(m):
        a, b, c = map(int, input().split())
        routes.append((a - 1, b - 1, c))

    friends, capacity = map(int, input().split())
    graph = [[] for _ in range(n)]

    def add_edge(a, b, cap, cost):
        graph[a].append([b, cap, cost, len(graph[b])])
        graph[b].append([a, 0, -cost, len(graph[a]) - 1])

    for a, b, cost in routes:
        add_edge(a, b, capacity, cost)
        add_edge(b, a, capacity, cost)

    source = 0
    target = n - 1
    flow = 0
    total_cost = 0
    potential = [0] * n
    infinity = 10 ** 30

    while flow < friends:
        distance = [infinity] * n
        previous_vertex = [-1] * n
        previous_edge = [-1] * n
        distance[source] = 0
        heap = [(0, source)]

        while heap:
            current_distance, vertex = heappop(heap)
            if current_distance != distance[vertex]:
                continue

            for edge_index, edge in enumerate(graph[vertex]):
                destination, remaining, cost, reverse = edge
                if remaining == 0:
                    continue

                new_distance = current_distance + cost + potential[vertex] - potential[destination]
                if new_distance < distance[destination]:
                    distance[destination] = new_distance
                    previous_vertex[destination] = vertex
                    previous_edge[destination] = edge_index
                    heappush(heap, (new_distance, destination))

        if distance[target] == infinity:
            break

        for vertex in range(n):
            if distance[vertex] < infinity:
                potential[vertex] += distance[vertex]

        sent = friends - flow
        vertex = target
        while vertex != source:
            parent = previous_vertex[vertex]
            edge_index = previous_edge[vertex]
            sent = min(sent, graph[parent][edge_index][1])
            vertex = parent

        vertex = target
        path_cost = 0
        while vertex != source:
            parent = previous_vertex[vertex]
            edge_index = previous_edge[vertex]
            edge = graph[parent][edge_index]
            path_cost += edge[2]
            edge[1] -= sent
            graph[vertex][edge[3]][1] += sent
            vertex = parent

        flow += sent
        total_cost += sent * path_cost

    print(f"Instancia {instance}")
    if flow == friends:
        print(total_cost)
    else:
        print("impossivel")
    print()

    instance += 1
