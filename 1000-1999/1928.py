n = int(input())
cards = list(map(int, input().split()))

pairs = [None] * (n // 2 + 1)
for position, number in enumerate(cards):
    if pairs[number] is None:
        pairs[number] = [position, -1]
    else:
        pairs[number][1] = position

graph = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)

levels = n.bit_length()
parent = [[-1] * n for _ in range(levels)]
depth = [0] * n
stack = [0]
order = [0]

while stack:
    node = stack.pop()
    for neighbor in graph[node]:
        if neighbor != parent[0][node]:
            parent[0][neighbor] = node
            depth[neighbor] = depth[node] + 1
            stack.append(neighbor)
            order.append(neighbor)

for level in range(1, levels):
    previous = parent[level - 1]
    current = parent[level]
    for node in range(n):
        ancestor = previous[node]
        if ancestor != -1:
            current[node] = previous[ancestor]

def lca(a, b):
    if depth[a] < depth[b]:
        a, b = b, a

    difference = depth[a] - depth[b]
    level = 0
    while difference:
        if difference & 1:
            a = parent[level][a]
        difference >>= 1
        level += 1

    if a == b:
        return a

    for level in range(levels - 1, -1, -1):
        if parent[level][a] != parent[level][b]:
            a = parent[level][a]
            b = parent[level][b]

    return parent[0][a]

total = 0
for a, b in pairs[1:]:
    ancestor = lca(a, b)
    total += depth[a] + depth[b] - 2 * depth[ancestor]

print(total)
