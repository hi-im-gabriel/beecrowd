def integers():
    data = open(0, "rb").read()
    number = 0
    reading = False
    for byte in data:
        if 48 <= byte <= 57:
            number = number * 10 + byte - 48
            reading = True
        elif reading:
            yield number
            number = 0
            reading = False
    if reading:
        yield number

values = iter(integers())
outputs = []

while True:
    try:
        n = next(values)
        m = next(values)
    except StopIteration:
        break

    edges_by_cost = [[] for _ in range(10001)]
    for _ in range(m):
        a = next(values) - 1
        b = next(values) - 1
        cost = next(values)
        edges_by_cost[cost].append(a * n + b)

    parent = list(range(n))
    size = [1] * n

    def find(node):
        while node != parent[node]:
            parent[node] = parent[parent[node]]
            node = parent[node]
        return node

    total = 0
    used = 0

    for cost in range(1, 10001):
        for edge in edges_by_cost[cost]:
            a, b = divmod(edge, n)
            root_a = find(a)
            root_b = find(b)

            if root_a != root_b:
                if size[root_a] < size[root_b]:
                    root_a, root_b = root_b, root_a
                parent[root_b] = root_a
                size[root_a] += size[root_b]
                total += cost
                used += 1

                if used == n - 1:
                    break
        if used == n - 1:
            break

    if used == n - 1:
        outputs.append(str(total))
    else:
        outputs.append("impossivel")

print("\n".join(outputs))
