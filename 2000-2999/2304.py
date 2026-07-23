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
I, N = map(int, input().split())
result = {
    'D': I,
    'E': I,
    'F': I,
}
for _ in range(N):
    s = input().split()
    if len(s) == 4:
        op, p1, p2, amount = s
        result[p1] += int(amount)
        result[p2] -= int(amount)
    else:
        op, p1, amount = s
        if op == 'C':
            result[p1] -= int(amount)
        else:
            result[p1] += int(amount)
values = ' '.join(str(v) for v in result.values())
print(values)
