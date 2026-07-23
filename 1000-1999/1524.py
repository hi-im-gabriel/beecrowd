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
while True:
    try:
        N, K = map(int, input().split())
        positions = [0] + list(map(int, input().split()))
        gaps = [positions[i] - positions[i - 1] for i in range(1, N)]
        gaps.sort(reverse=True)
        total_span = positions[-1] - positions[0]
        result = total_span - sum(gaps[:K - 1])
        print(result)
    except EOFError:
        break
