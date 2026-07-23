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
#n= list(map(int,input().split()))
#string.append(input()) array
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfabeto
n = int(input())
raio = 0
i = 502
q = [[0] * i for x in range(i)]
while n:
    n -= 1
    x, y = [int(i) for i in input().split()]
    if not raio:
        if q[int(x)][int(y)] == 0:
            q[int(x)][int(y)] = 1
        else:
            raio = 1
print(raio)
