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
#n= list(map(int,input().split()))
#string.append(input()) array
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfabeto
while True:
    try:
        n = int(input())
        s = {}
        while n:
            n -= 1
            carne = input().split()
            s[carne[0]] = int(carne[1])
        s = {k: v for k, v in sorted(s.items(), key=lambda x: x[1])}
        
        print(*s)
    except EOFError:
        break
