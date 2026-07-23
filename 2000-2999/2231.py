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
test = 1
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    l = []
    for _ in range(n):
        l.append(int(input()))
    avgs = []
    window_sum = sum(l[:m])
    avgs.append(int(window_sum / m))
    for i in range(1, n - m + 1):
        window_sum = window_sum - l[i - 1] + l[i + m - 1]
        avgs.append(int(window_sum / m))
    print(f"Teste {test}")
    print(f"{min(avgs)} {max(avgs)}")
    print()
    test += 1
