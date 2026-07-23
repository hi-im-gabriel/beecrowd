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
40
41
42
43
44
#x=list(map(int,input().split()))
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfa
#d=dict()
#d[key]=s[value]
#d=dict(sorted(d.items(), key=lambda item: item[1]))
from math import sqrt
tipo = {
'fire':  {'dmg': 200, 'n1': 20, 'n2': 30, 'n3': 50},
'water': {'dmg': 300, 'n1': 10, 'n2': 25, 'n3': 40},
'earth': {'dmg': 400, 'n1': 25, 'n2': 55, 'n3': 70},
'air':   {'dmg': 100, 'n1': 18, 'n2': 38, 'n3': 60}}
for g in range(int(input())):
   w,h,x0,y0=map(int,input().split())
   e=input().split()
   n,cx,cy=[int(x) for x in e[1:]]
   enum=tipo[e[0]]
   dmg=enum['dmg']
   ns='n' + str(n)
   r=enum[ns]
   aux=True
   if x0 <= cx <= x0+w and y0 <= cy <= y0+h:aux=False
   if aux:
      c1 = (y0-cy)**2
      c2 = (y0+h-cy)**2
      for px in range(x0, x0+w+1):
         d1 = sqrt((px-cx)**2 + c1)
         d2 = sqrt((px-cx)**2 + c2)
         if r >= d1 or r >= d2:
            aux = False
            break
   if aux:
      c1,c2=(x0-cx)**2,(x0+w-cx)**2
      for py in range(y0, y0+h+1):
         d1,d2=sqrt(c1 + (py-cy)**2),sqrt(c2 + (py-cy)**2)
         if r>=d1 or r>=d2:
            aux=False
            break
   if aux:print(0)
   else:print(dmg)
