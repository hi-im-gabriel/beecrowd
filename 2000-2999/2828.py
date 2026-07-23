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
#n=list(map(int,input().split()))
#s.pop() remover ultimo elemento
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfa
from math import factorial
big = 10**9 + 7
palavra = input()
occ = {}
for c in palavra:
    if c in occ:
        occ[c] += 1
    else:
        occ[c] = 1
cima = 0
baixo = 1
for c in occ:
    cima += occ[c]
    baixo *= factorial(occ[c])
aux = factorial(cima)//baixo
aux = pow(aux, 1, big)
print(aux)
