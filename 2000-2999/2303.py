L, C, M, N = map(int, input().split())

maximum = 0
column_sums = [0] * C

for row in range(L):
    values = list(map(int, input().split()))

    for column in range(C):
        column_sums[column] += values[column]

    if (row + 1) % M == 0:
        for start in range(0, C, N):
            total = sum(column_sums[start:start + N])
            if total > maximum:
                maximum = total

        column_sums = [0] * C

print(maximum)
