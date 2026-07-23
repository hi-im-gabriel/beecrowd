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
28
#n=list(map(int,input().split()))
#s.pop() remover ultimo elemento
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfa
b = []
for i in range(32):
    if(i<10):
        b.append(i)
    else:
        b.append(chr(i+55))
while(True):
    n = int(input())
    if n==0:
        print(n)
        break
    aux = ''
    while(n > 31):
        i = int(n%32)
        aux += str(b[i])
        n /= 32
    aux += str(b[int(n)])
    aux = aux[::-1]
    print(aux)
