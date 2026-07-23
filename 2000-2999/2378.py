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
#n=list(map(int,input().split()))
#s.pop() remover ultimo elemento
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfa
#d=dict()
#d[key]=s[value]
#d=dict(sorted(d.items(), key=lambda item: item[1]))
n,c=map(int,input().split())
pessoas=0
aux=False
for i in range(n):
   s,e=map(int,input().split())
   pessoas+=e-s
   if pessoas>c:aux=True
print("S") if aux else print("N")
