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
casos = int(input())
i = 0
while i < casos:
    nome, lv = [x for x in input().split()]
    stats = []
    for j in range(0,4):
        bs, iv, ev = [int(x) for x in input().split()]
        s = 0
        if j == 0:
            s = ((iv + bs + (ev**0.5)/8 + 50) * int(lv))/ 50 + 10
        else:
            s = ((iv + bs + (ev**0.5)/8) * int(lv))/ 50 + 5
        stats.append(s)
    i += 1
    print("Caso #%d: %s nivel %d" % (i, nome, int(lv)))
    print("HP: %d" % (stats[0]))
    print("AT: %d" % (stats[1]))
    print("DF: %d" % (stats[2]))
    print("SP: %d" % (stats[3]))
