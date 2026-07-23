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
31
#n=list(map(int,input().split()))
#s.pop() remover ultimo elemento
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfabeto
while True:
    prob =[0] * 26
    dorm =[0] * 26
    s=aux=0
    n = int(input())
    if not n:
        break
    while n:
        n -= 1
        p, t, j = input().split()
        pos = ord(p) - 65
        if j == "correct":
            s += 1
            aux += int(t)
            prob[pos] = 1
        if j == "incorrect":
            dorm[pos] += 20
    for pos in range(len(prob)):
        if prob[pos]:
            aux += dorm[pos]
    print(s, aux)
