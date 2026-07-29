while True:
    try:
        n, k = map(int, input().split())
    except EOFError:
        break

    if n == 0 and k == 0:
        break

    sequence = list(map(int, input().split()))
    counts = [1] * n

    for _ in range(1, k):
        next_counts = [0] * n

        for i in range(n):
            for j in range(i):
                if sequence[j] < sequence[i]:
                    next_counts[i] += counts[j]

        counts = next_counts

    print(sum(counts))
