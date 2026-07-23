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
#string.append(input()) array
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfabeto
aux = 0
for n in range(int(input())):
    n -= 1
    m, c = [int(x) for x in input().split()]
    hash = {str(x) : [] for x in range(m)}
    entrada = [int(x) for x in input().split()]
    if aux:
        print()
    for i in entrada:
        resto = i % m
        hash[str(resto)].append(int(i))
    for i in hash:
        print("%d -> " % int(i), end = "")
        for j in hash[i]:
            print("%d -> " % j, end = "")
        print("\\")
    aux = 1
