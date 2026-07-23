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
    s = []
    n = int(input())
    while(n > 0):
        n -= 1
        s.append(input())
    aux = s[0]
    for n in s:
        if n != aux:
            aux = 'ingles'
            break
    print(aux)
