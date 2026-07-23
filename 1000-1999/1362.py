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
def calc(p):
    global found
    if p == m + 1:
        found = True
        return
    if found:
        return
    if qtde[tipo[p][0]]:
        qtde[tipo[p][0]] -= 1
        calc(p + 1)
        qtde[tipo[p][0]] += 1
    if qtde[tipo[p][1]]:
        qtde[tipo[p][1]] -= 1
        calc(p + 1)
        qtde[tipo[p][1]] += 1
def val(s):
    sizes = ["XS", "S", "M", "L", "XL", "XXL"]
    return sizes.index(s) + 1
global m, found, qtde, tipo
cases = int(input())
for _ in range(cases):
    n, m = map(int, input().split())
    qtde = [n // 6] * 10
    tipo = [[0, 0]] * (m + 1)
    for i in range(1, m + 1):
        s1, s2 = input().split()
        tipo[i] = [val(s1), val(s2)]
    found = False
    calc(1)
    if found:
        print("YES")
    else:
        print("NO")
