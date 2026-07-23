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
#n=list(map(int,input().split()))
#s.pop() remover ultimo elemento
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfa
from math import sqrt
for i in range(int(input())):
    n = int(input())
    x,y=map(int,input().split())
    perto = 999999999
    for cont in range(n):
        n -= 1
        xb, yb = [int(i) for i in input().split()]
        d = sqrt(abs(x - xb)**2 + abs(y - yb)**2)
        if d < perto:
            perto = d
            pos = cont + 1
    print(pos)
