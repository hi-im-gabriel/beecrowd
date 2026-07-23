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
#n=list(map(int,input().split()))
#s.pop() remover ultimo elemento
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfa
while True:
    n,d=map(int,input().split())
    if n==d==0:break
    l = []
    s = 'no'
    jantar = [0] * int(n)
    for i in range(int(d)):
        l.append([int(x) for x in input().split()])
        for j in range(int(n)):
            if l[i][j] == 1:
                jantar[j] += 1
    if jantar.count(int(d)) > 0:
        s = 'yes'
    print(s)
