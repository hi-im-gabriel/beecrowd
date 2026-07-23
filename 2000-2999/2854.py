def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    ra, rb = find(a), find(b)
    if ra != rb:
        parent[rb] = ra


M, N = map(int, input().split())

parent = {}
present = set()

for i in range(1, N + 1):
    a, _, b = input().split()
    present.add(a)
    present.add(b)
    if a not in parent:
        parent[a] = a
    if b not in parent:
        parent[b] = b
    union(a, b)

components = set()
for p in present:
    components.add(find(p))

families_with_relations = len(components)

isolated = M - len(present)

print(families_with_relations + isolated)
