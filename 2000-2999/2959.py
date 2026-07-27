n, m, p = map(int, input().split())

parent = list(range(n + 1))
size = [1] * (n + 1)


def find(neighborhood):
    while neighborhood != parent[neighborhood]:
        parent[neighborhood] = parent[parent[neighborhood]]
        neighborhood = parent[neighborhood]
    return neighborhood


for _ in range(m):
    a, b = map(int, input().split())
    root_a = find(a)
    root_b = find(b)

    if root_a != root_b:
        if size[root_a] < size[root_b]:
            root_a, root_b = root_b, root_a
        parent[root_b] = root_a
        size[root_a] += size[root_b]

for _ in range(p):
    k, l = map(int, input().split())
    if find(k) == find(l):
        print("Lets que lets")
    else:
        print("Deu ruim")
