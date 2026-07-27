n = int(input())

parent = list(range(n))
size = [1] * n
parity = [0] * n


def find(x):
    if parent[x] != x:
        previous = parent[x]
        parent[x] = find(previous)
        parity[x] ^= parity[previous]
    return parent[x]


possible = True

for i in range(n):
    row = list(map(int, input().split()))

    if possible:
        for j, share_dialect in enumerate(row):
            if i != j and share_dialect == 0:
                root_i = find(i)
                parity_i = parity[i]
                root_j = find(j)
                parity_j = parity[j]

                if root_i == root_j:
                    if parity_i == parity_j:
                        possible = False
                        break
                else:
                    if size[root_i] < size[root_j]:
                        root_i, root_j = root_j, root_i
                        parity_i, parity_j = parity_j, parity_i

                    parent[root_j] = root_i
                    parity[root_j] = parity_i ^ parity_j ^ 1
                    size[root_i] += size[root_j]

print("Bazinga!" if possible else "Fail!")
