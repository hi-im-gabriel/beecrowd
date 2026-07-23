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
#n=list(map(int,input().split()))
#s.pop() remover ultimo elemento
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfa
from math import ceil
for i in range(int(input())):
    n,m=map(float,input().split())
    print(ceil(n/m))
