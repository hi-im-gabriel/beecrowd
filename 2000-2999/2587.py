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
#n=list(map(int,input().split()))
#s.pop() remover ultimo elemento
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfa
def aux(x, p):
    for i in range(len(p)):
        if p[i] == '_': continue
        if not x[i] == p[i]: return False
    return True
for g in range(int(input())):
    a = str(input())
    b = str(input())
    p = str(input())
    a1 = a[p.find('_')]
    a2 = a[p.rfind('_')]
    b1 = b[p.find('_')]
    b2 = b[p.rfind('_')]
    if aux(a, p) and aux(b, p):
        print('Y' if a == b or (a2 == b1 or a1 == b2) else 'N')
    else: print('Y')
