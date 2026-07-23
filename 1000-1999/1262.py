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
29
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
        m = input()
        n = int(input())
        tot = 0
        aux = n
        for i in range(len(m)):
            if m[i] == 'R':
                if aux == n:
                    tot += 1
                if not aux != 0:
                    aux = n
                    tot += 1
                aux -= 1
            elif not m[i] != 'W':
                tot += 1
                aux = n
        print(tot)
    except EOFError:
        break
