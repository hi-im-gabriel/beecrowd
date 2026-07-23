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
#n= list(map(int,input().split()))
#string.append(input()) array
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfabeto
vitC,empC,salC,vitF,empF,salF=map(int,input().split())
pontosC=(vitC*3)+(empC)
pontosF=(vitF*3)+(empF)
if pontosC>pontosF:
    print("C")
elif pontosF>pontosC:
    print("F")
else:
    if salF>salC:
        print("F")
    elif salC>salF:
        print("C")
    else:
        print("=")
