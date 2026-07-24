t = int(input())

for _ in range(t):
    n = int(input())
    permutation = list(map(int, input().split()))
    visited = [False] * n
    swaps = 0

    for i in range(n):
        if visited[i] or permutation[i] == i + 1:
            continue

        cycle_size = 0
        j = i

        while not visited[j]:
            visited[j] = True
            j = permutation[j] - 1
            cycle_size += 1

        swaps += cycle_size - 1

    print(swaps)
