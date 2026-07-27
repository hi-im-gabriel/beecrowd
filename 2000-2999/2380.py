n, k = map(int, input().split())

parent = list(range(n + 1))
size = [1] * (n + 1)


def find(bank):
    while bank != parent[bank]:
        parent[bank] = parent[parent[bank]]
        bank = parent[bank]
    return bank


for _ in range(k):
    operation, bank_a, bank_b = input().split()
    bank_a = int(bank_a)
    bank_b = int(bank_b)

    root_a = find(bank_a)
    root_b = find(bank_b)

    if operation == "F":
        if size[root_a] < size[root_b]:
            root_a, root_b = root_b, root_a
        parent[root_b] = root_a
        size[root_a] += size[root_b]
    elif root_a == root_b:
        print("S")
    else:
        print("N")
