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
def x(s):
   return [c for c in s]
def ver(n,m):
   if n>m:print("1")
   elif m>n:print("2")
   else:print("0")
while True:
   n,m=input().split()
   if n==m=='0':break
   while len(n)>1 or len(m)>1:
      aux=map(int,x(n))
      aux1=map(int,x(m))
      n=str(sum(aux))
      m=str(sum(aux1))
   
   ver(int(n),int(m))
