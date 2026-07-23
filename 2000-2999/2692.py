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
#n=list(map(int,input().split()))
#s.pop() remover ultimo elemento
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfa
casos,vezes = map(int,input().split())
letras=[]
letras_aux=[]
for i in range(casos):
    letra_1,letra_2 = input().split()
    letras.append(letra_1)
    letras_aux.append(letra_2)
for a in range(vezes):
    texto = input()
    texto=list(texto) 
   
    for j in range(len(texto)):
        for k in range(casos):
            if texto[j] == letras[k]:
                texto[j]=letras_aux[k]
   
            elif texto[j] == letras_aux[k]:
              texto[j]=letras[k]
   
    for m in texto:
      print(m,end="")
    print()
