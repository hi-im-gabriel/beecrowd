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
# -*- coding: utf-8 -*-
'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''#n= list(map(int,input().split()))
#string.append(input()) array
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
n = int(input())
let = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 's', 'S']
while n:
    c = input()
    aux = 1
    for i in range(len(c)):
        if c[i] in let:
            aux *= 3
        else:
            aux *= 2
    print(aux)
    n-=1
