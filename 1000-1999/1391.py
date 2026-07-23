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
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
import heapq
INF = 10**18
def dijkstra(start, adj, n):
    dist = [INF] * n
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in adj[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    return dist
while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break
    S, D = map(int, input().split())
    adj = [[] for _ in range(N)]
    radj = [[] for _ in range(N)]
    for _ in range(M):
        u, v, p = map(int, input().split())
        adj[u].append((v, p))
        radj[v].append((u, p))
    dist = dijkstra(S, adj, N)
    if dist[D] == INF:
        print(-1)
        continue
    removed = [[False]*len(adj[u]) for u in range(N)]
    queue = [D]
    visited = [False]*N
    visited[D] = True
    while queue:
        v = queue.pop(0)
        for u, w in radj[v]:
            if dist[u] + w == dist[v]:
                for i, (to, _) in enumerate(adj[u]):
                    if to == v:
                        removed[u][i] = True
                if not visited[u]:
                    visited[u] = True
                    queue.append(u)
    new_adj = [[] for _ in range(N)]
    for u in range(N):
        for i, (v, w) in enumerate(adj[u]):
            if not removed[u][i]:
                new_adj[u].append((v, w))
    dist2 = dijkstra(S, new_adj, N)
    print(dist2[D] if dist2[D] != INF else -1)
