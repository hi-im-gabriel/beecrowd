while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break

    cnt = [0] * 10001

    for _ in range(N):
        ranking = list(map(int, input().split()))
        for x in ranking:
            cnt[x] += 1

    max1 = 0
    max2 = 0

    for i in range(1, 10001):
        if cnt[i] > max1:
            max2 = max1
            max1 = cnt[i]
        elif max2 < cnt[i] < max1:
            max2 = cnt[i]

    result = []
    for i in range(1, 10001):
        if cnt[i] == max2:
            result.append(str(i))

    print(" ".join(result) + " ")
