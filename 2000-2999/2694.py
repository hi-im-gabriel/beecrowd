#n= list(map(int,input().split()))
#string.append(input()) array
#s=sorted(s,key=len,reverse=True)
#print(*s,sep=" ")
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
import re
n=int(input())
while n:
    s=input()
    s=re.sub(r"[^0-9 ]"," ",s)
    s=s.split()
    print(int(s[0])+int(s[1])+int(s[2]))
    n-=1
