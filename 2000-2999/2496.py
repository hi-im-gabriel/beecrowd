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
#s.pop() remover ultimo elemento
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfa
m = int(input())
alph = []
for i in range(65, 91):
    alph.append(chr(i))
for j in range(m):
    total = 0
    n = int(input())
    a = input()
    for i in range(n):
        if(a[i] != alph[i]):
            total += 1
    if(total < 3):
        print("There are the chance.")
    else:
        print("There aren't the chance.")
