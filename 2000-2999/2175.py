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
#import string
#alfa = list(string.ascii_lowercase) lsit do alfabeto
o,b,i=map(float,input().split())
if o<b and o<i:
    print("Otavio")
elif b<o and b<i:
    print("Bruno")
elif i<o and i<b:
    print("Ian")
else:
    print("Empate")
