import sys

readline = sys.stdin.buffer.readline
outputs = []

while True:
    line = readline()

    if not line:
        break

    if not line.strip():
        continue

    n, m = map(int, line.split())
    parent = [-1] * (n + 1)

    def find(element):
        root = element

        while parent[root] >= 0:
            root = parent[root]

        while element != root:
            next_element = parent[element]
            parent[element] = root
            element = next_element

        return root

    for _ in range(m):
        a, b = map(int, readline().split())

        root_a = find(a)
        root_b = find(b)

        if root_a != root_b:
            if parent[root_a] > parent[root_b]:
                root_a, root_b = root_b, root_a

            parent[root_a] += parent[root_b]
            parent[root_b] = root_a

    species = int(readline())
    outputs.append(str(-parent[find(species)]))

sys.stdout.write("\n".join(outputs) + "\n")
