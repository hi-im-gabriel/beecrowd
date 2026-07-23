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
inst = 1
first = True
while True:
    line = input()
    if not line:
        break
    n = int(line.strip())
    if n == 0:
        break
    stats = [[0, 0, 0] for _ in range(n + 1)]
    games = n * (n - 1) // 2
    for _ in range(games):
        x, y, z, w = map(int, input().split())
        if y > w:
            stats[x][0] += 2
            stats[z][0] += 1
        else:
            stats[z][0] += 2
            stats[x][0] += 1
        stats[x][1] += y
        stats[x][2] += w
        stats[z][1] += w
        stats[z][2] += y
    def cesta_average(i):
        scored, conceded = stats[i][1], stats[i][2]
        if conceded == 0:
            return float(scored)
        return scored / conceded
    teams = list(range(1, n + 1))
    teams.sort(
        key=lambda i: (
            -stats[i][0],
            -cesta_average(i),
            -stats[i][1],
            i
        )
    )
    if not first:
        print()
    first = False
    print(f"Instancia {inst}")
    print(" ".join(map(str, teams)))
    inst += 1
