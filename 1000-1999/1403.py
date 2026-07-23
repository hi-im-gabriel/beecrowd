1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
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
