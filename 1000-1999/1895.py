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
#n=list(map(int,input().split()))
#s.pop() remover ultimo elemento
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfabeto
n,t,v=map(int,input().split())
A=B=aux=0
for x in range (n-1):
    s = int(input())
    if abs(t - s)<= v:
        if aux==0:
            A+= abs(t - s)
        else:
            B+= abs(t-s)
        t = s
    if aux==0:
        aux = 1
    else:
        aux=0
print(A,B)
