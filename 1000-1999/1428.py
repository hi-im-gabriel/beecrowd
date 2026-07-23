#n= list(map(int,input().split()))
#string.append(input()) array
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
from math import ceil

t=int(input())
while t:
    a,b=map(int,input().split())
    print(ceil((a-2)/3)*ceil((b-2)/3))
    t-=1
