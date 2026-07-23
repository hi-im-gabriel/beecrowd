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
n = int(input())
for nIndex in range(n):
    nams = []
    vals = []
    total = 0.0
    n2 = int(input())
    for n2Index in range(n2):
        nam, val = input().split(' ')
        nams.insert(len(nams), nam)
        vals.insert(len(vals), float(val))
    n2 = int(input())
    for n2Index in range(n2):
        nam, quant = input().split(' ')
        total += vals[nams.index(nam)] * int(quant)
    print ("R$ %.2f" % total)
