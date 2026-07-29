n, l = map(int, input().split())

parent = list(range(n + 1))


def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x


for _ in range(l):
    x, y = map(int, input().split())
    root_x = find(x)
    root_y = find(y)
    parent[root_y] = root_x

root = find(1)

if all(find(segment) == root for segment in range(2, n + 1)):
    print("COMPLETO")
else:
    print("INCOMPLETO")
