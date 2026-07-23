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
for i in range(int(input())):
    aux=0
    s=list(input())
    if i ==0:
        tam=len(s)
    if s[0]=='R' and s[1]=='A' and len(s)==tam:
        s.remove('R')
        s.remove('A')
        prov= ''.join(map(str,s))
        print(int(prov))
    else:
        print("INVALID DATA")
