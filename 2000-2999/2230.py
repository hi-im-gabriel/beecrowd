test = 1

while True:
    cities, roads, location, max_tolls = map(int, input().split())

    if cities == roads == location == max_tolls == 0:
        break

    graph = [[] for _ in range(cities + 1)]

    for _ in range(roads):
        city_a, city_b = map(int, input().split())
        graph[city_a].append(city_b)
        graph[city_b].append(city_a)

    distances = [-1] * (cities + 1)
    distances[location] = 0

    queue = [location]
    index = 0

    while index < len(queue):
        current = queue[index]
        index += 1

        if distances[current] == max_tolls:
            continue

        for neighbor in graph[current]:
            if distances[neighbor] == -1:
                distances[neighbor] = distances[current] + 1
                queue.append(neighbor)

    reachable = [
        str(city)
        for city in range(1, cities + 1)
        if city != location and 0 < distances[city] <= max_tolls
    ]

    print(f"Teste {test}")
    print(" ".join(reachable) + (" " if reachable else ""))
    print()

    test += 1
