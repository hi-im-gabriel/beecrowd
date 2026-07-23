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
#alfa = list(string.ascii_lowercase) lsit do alfabeto
for i in range(int(input())):
    dieta = input()
    cafe = input()
    almoco = input()
    almoco += cafe
    for letra in range(len(almoco)):
        if almoco[letra] not in dieta:
            dieta = "CHEATER"
            break
        else:
            dieta = dieta.replace(almoco[letra], "")
    if dieta != "CHEATER":
        dieta = "".join(sorted(dieta))
    print(dieta)
