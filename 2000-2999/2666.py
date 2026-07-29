n, capacity = map(int, input().split())
gold = list(map(int, input().split()))
roads = [[] for _ in range(n)]

for _ in range(n - 1):
    a, b, distance = map(int, input().split())
    a -= 1
    b -= 1
    roads[a].append((b, distance))
    roads[b].append((a, distance))

parent = [-1] * n
parent_distance = [0] * n
order = [0]

for city in order:
    for neighbor, distance in roads[city]:
        if neighbor != parent[city]:
            parent[neighbor] = city
            parent_distance[neighbor] = distance
            order.append(neighbor)

answer = 0

for city in reversed(order[1:]):
    answer += 2 * parent_distance[city] * ((gold[city] + capacity - 1) // capacity)
    gold[parent[city]] += gold[city]

print(answer)
