while True:
    n = int(input())
    if n == 0:
        break

    columns = [[] for _ in range(n)]
    for _ in range(n):
        row = list(map(int, input().split()))
        for j, value in enumerate(row):
            columns[j].append(value)

    dp = [0]
    total = 0
    for value in columns[0]:
        total += value
        dp.append(total)

    for column in columns[1:]:
        suffix_maximum = [0] * len(dp)
        best = dp[-1]
        for height in range(len(dp) - 1, -1, -1):
            if dp[height] > best:
                best = dp[height]
            suffix_maximum[height] = best

        new_dp = [suffix_maximum[0]]
        total = 0
        for height, value in enumerate(column, 1):
            total += value
            new_dp.append(total + suffix_maximum[height])
        dp = new_dp

    print(max(dp))
