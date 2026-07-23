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
#n= list(map(int,input().split()))
#string.append(input()) array
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfabeto
while True:
    n=int(input())
    if n==0:
        break
    aux=10
    s=list(map(int,input().split()))
    i=1
    while i<n:
        aux+=min(10,s[i]-s[i-1])
        i+=1
    print(aux)
