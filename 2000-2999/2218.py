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
#n= list(map(int,input().split()))
#string.append(input()) array
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
aux=[1]
for i in range(1, 2**16):
    aux.append(i+aux[i-1])
n=int(input())
while n:
    m=int(input())
    print(aux[m])
    n-=1
