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
N = int(input())
grid = [input().strip() for _ in range(N)]
current = 0
best = 0
for i in range(N):
    cols = range(N) if i % 2 == 0 else range(N - 1, -1, -1)
    for j in cols:
        if grid[i][j] == 'o':
            current += 1
            if current > best:
                best = current
        elif grid[i][j] == 'A':
            current = 0
print(best)
