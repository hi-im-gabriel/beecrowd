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
#n=list(map(int,input().split()))
#string.append(input()) array
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfabeto
while True:
    n, m = input().split()
    n, m = int(n), int(m)
    if n == m == 0:
        break
    carac = 4
    competidor = []
    for i in range(n):
        competidor.append([int(x) for x in input().split()])
    for i in range(n):
        p = competidor[i].count(1)
        if p == m:
            carac -= 1
            break
    problema = [0] * m
    for i in range(n):
        for j in range(m):
            if competidor[i][j] == 1:
                problema[j] += 1
    if problema.count(0) > 0:
        carac -= 1
    for j in range(m):
        if problema[j] == n:
            carac -= 1
            break
    for i in range(n):
        p = competidor[i].count(0)
        if p == m:
            carac -= 1
            break
    print(carac)
