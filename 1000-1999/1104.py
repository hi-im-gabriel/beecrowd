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
#n=list(map(int,input().split()))
#string.append(input()) array
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfabeto
while True:
    a,b=input().split()
    if a==b=='0':
        break
    fa=[int(x) for x in input().split()]
    fb=[int(x) for x in input().split()]
    a=set(fa)
    b=set(fb)
    c=b
    f=0
    if len(a)<len(b):
        c=a
        a=b
    c=[x for x in c if x not in a]
    print(len(c))
