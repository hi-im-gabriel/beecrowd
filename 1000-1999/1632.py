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
