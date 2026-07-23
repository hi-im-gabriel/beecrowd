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
#n=list(map(int,input().split()))
#s.pop() remover ultimo elemento
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfabeto
n=int(input())
v=input().split()
aux=1
aux2=1
for i in range(1,n):
    if v[i]==v[i-1]:
        aux2+=1
    else:
        if aux2>aux:
            aux=aux2
        aux2=1
if aux2>aux:
    aux=aux2
print(aux)
