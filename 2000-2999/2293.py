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
36
37
38
39
40
41
42
43
44
45
46
47
48
#n=list(map(int,input().split()))
#s.pop() remover ultimo elemento
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfa
#d=dict()
#d[key]=s[value]
#d=dict(sorted(d.items(), key=lambda item: item[1]))
n,m=map(int,input().split())
matriz = []
for i in range(n):
    linha = input()
    lista_str = linha.split()
    lista_int = []
    for x in lista_str:
        lista_int.append(int(x))
    matriz.append(lista_int)
melhor = None
for i in range(n):
    soma = 0
    for j in range(m):
        soma += matriz[i][j]
    if melhor == None:
        melhor = soma
    else:
        melhor = max(melhor, soma)
for j in range(m):
    soma = 0
    for i in range(n):
        soma += matriz[i][j]
    melhor = max(melhor, soma)
print(melhor)
