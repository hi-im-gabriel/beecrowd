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
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
def floodfill(r, c, c1, c2):
    global R, C, grid
    if r < 0 or r >= R or c < 0 or c >= C:
        return 0
    if grid[r][c] != c1:
        return 0
    ans = 1
    grid[r][c] = c2
    for d in range(4):
        ans += floodfill(r + dr[d], c + dc[d], c1, c2)
    return ans
while True:
    R, C = map(int, input().split())
    
    if R == 0 and C == 0:
        break
    
    grid = []
    row = []
    col = []
    
    for _ in range(R):
        row_input = input().strip()
        grid.append(list(row_input))
        for j in range(C):
            if row_input[j] == 'T':
                grid[_][j] = 'A'
                row.append(_)
                col.append(j)
    
    for i in range(len(col)):
        floodfill(row[i], col[i], 'A', 'T')
    
    for i in range(R):
        print(''.join(grid[i]))
    print()
