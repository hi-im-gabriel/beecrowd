#n=list(map(int,input().split()))
#s.pop() remover ultimo elemento
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfabeto
from math import sqrt
l,a,p,r=map(int,input().split())
r=r+r
d=sqrt((l*l)+(a*a)+(p*p))
if d<=r:
    print("S")
else:
    print("N")
