while True:
    try:
        line = input()
        while not line.strip():
            line = input()
        n, c, t1, t2 = map(int, line.split())
        holes = sorted(set(map(int, input().split())))
    except EOFError:
        break

    m = len(holes)
    extended = holes + [position + c for position in holes]

    next1 = [0] * (2 * m)
    next2 = [0] * (2 * m)

    right1 = 0
    right2 = 0
    for left in range(2 * m):
        if right1 < left + 1:
            right1 = left + 1
        limit = extended[left] + t1
        while right1 < 2 * m and extended[right1] <= limit:
            right1 += 1
        next1[left] = right1

        if right2 < left + 1:
            right2 = left + 1
        limit = extended[left] + t2
        while right2 < 2 * m and extended[right2] <= limit:
            right2 += 1
        next2[left] = right2

    infinite = 10 ** 18
    answer = infinite

    for start in range(m):
        end = start + m
        dp = [infinite] * (m + 1)
        dp[0] = 0

        for offset in range(m):
            current = dp[offset]
            if current >= answer:
                continue

            index = start + offset

            destination = next1[index]
            if destination > end:
                destination = end
            destination -= start
            cost = current + t1
            if cost < dp[destination]:
                dp[destination] = cost

            destination = next2[index]
            if destination > end:
                destination = end
            destination -= start
            cost = current + t2
            if cost < dp[destination]:
                dp[destination] = cost

        if dp[m] < answer:
            answer = dp[m]

    print(answer)
