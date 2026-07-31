m, n, k = map(int, input().split())

sensors = [tuple(map(int, input().split())) for _ in range(k)]
parent = list(range(k + 4))
size = [1] * (k + 4)

left = k
right = k + 1
bottom = k + 2
top = k + 3


def find(node):
    while node != parent[node]:
        parent[node] = parent[parent[node]]
        node = parent[node]
    return node


def union(a, b):
    root_a = find(a)
    root_b = find(b)

    if root_a == root_b:
        return

    if size[root_a] < size[root_b]:
        root_a, root_b = root_b, root_a

    parent[root_b] = root_a
    size[root_a] += size[root_b]


for i, (x, y, sensitivity) in enumerate(sensors):
    if x <= sensitivity:
        union(i, left)
    if m - x <= sensitivity:
        union(i, right)
    if y <= sensitivity:
        union(i, bottom)
    if n - y <= sensitivity:
        union(i, top)

    for j in range(i):
        other_x, other_y, other_sensitivity = sensors[j]
        distance_x = x - other_x
        distance_y = y - other_y
        sensitivity_sum = sensitivity + other_sensitivity

        if distance_x * distance_x + distance_y * distance_y <= sensitivity_sum * sensitivity_sum:
            union(i, j)

blocked = (
    find(left) == find(right)
    or find(bottom) == find(top)
    or find(left) == find(bottom)
    or find(right) == find(top)
)

print("N" if blocked else "S")
