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
30
#n=list(map(int,input().split()))
#s.pop() remover ultimo elemento
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfa
teste = 1
while True:
    v = int(input())
    if v == 0:
        break
    bits = ['0'] * 4
    if v >= 50:
        bits[0] = str(v // 50)
        v = v % 50
    if v >= 10:
        bits[1] = str(v // 10)
        v = v % 10
    if v >= 5:
        bits[2] = str(v // 5)
        v = v % 5
    bits[3] = str(v)
    print('Teste %d' % teste)
    print(' '.join(bits))
    print()
    teste += 1
