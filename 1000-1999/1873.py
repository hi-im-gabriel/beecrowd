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
33
34
35
#n= list(map(int,input().split()))
#string.append(input()) array
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfabeto
for i in range(int(input())):
    rajesh,sheldon=map(str,input().split())
    if rajesh == sheldon:
        print("empate")
    elif rajesh == "spock" and sheldon == "pedra":
        print("rajesh")
    elif rajesh == "lagarto" and sheldon == "spock":
        print("rajesh")
    elif rajesh == "tesoura" and sheldon == "lagarto":
        print("rajesh")
    elif rajesh == "papel" and sheldon == "spock":
        print("rajesh")
    elif rajesh == "tesoura" and sheldon == "papel":
        print("rajesh")
    elif rajesh == "papel" and sheldon == "pedra":
        print("rajesh")
    elif rajesh == "lagarto" and sheldon == "papel":
        print("rajesh")
    elif rajesh == "pedra" and sheldon == "lagarto":
        print("rajesh")
    elif rajesh == "spock" and sheldon == "tesoura":
        print("rajesh")
    elif rajesh == "pedra" and sheldon == "tesoura":
        print("rajesh")
    else:
        print("sheldon")
