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
30
31
32
import sys
sys.setrecursionlimit(10**7)
N, M = map(int, input().split())
parent = list(range(N + 1))
rank = [0] * (N + 1)
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]
def union(a, b):
    ra, rb = find(a), find(b)
    if ra == rb:
        return
    if rank[ra] < rank[rb]:
        parent[ra] = rb
    elif rank[ra] > rank[rb]:
        parent[rb] = ra
    else:
        parent[rb] = ra
        rank[ra] += 1
idx = 1
for _ in range(M):
    a, b = map(int, input().split())
    union(a, b)
families = set(find(i) for i in range(1, N + 1))
print(len(families))
