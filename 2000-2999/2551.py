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
32
#n=list(map(int,input().split()))
#s.pop() remover ultimo elemento
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfa
while True:
    try:
        n = int(input())
        treino = []
        recorde = []
        while n:
            n -= 1
            treino.append([int(x) for x in input().split()])
            if len(treino) == 1:
                media = treino[0][1]/treino[0][0]
                recorde.append(1)
            else:
                if treino[-1][1] / treino[-1][0] > media:
                    media = treino[-1][1] / treino[-1][0]
                    recorde.append(1)
                else:
                    recorde.append(0)
        for i in range(len(recorde)):
            if recorde[i] == 1:
                print(i + 1)
    except EOFError:
        break
