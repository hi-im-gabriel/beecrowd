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
#n=list(map(int,input().split()))
#string.append(input()) array
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfabeto
m = []
for i in range(4):
    m.append(str(input()))
v = []
for i in range(len(m[0])): 
    f = int(m[0][i]) * 1000
    f += int(m[1][i]) * 100
    f += int(m[2][i]) * 10
    f += int(m[3][i])
    v.append(f)
for i in range(1, len(v)-1):
    print(chr((v[0] * v[i] + v[-1]) % 257), end='')
print()
