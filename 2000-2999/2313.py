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
entrada = list(map(int, input().split()))
entrada.sort()
a,b,c = entrada
if(a+b<=c):
    print("Invalido")
else:
    if(a==b and b==c):
        tipo = "Valido-Equilatero"
    elif(a==b or b==c):
        tipo = "Valido-Isoceles"
    else:
        tipo = "Valido-Escaleno"
    if((pow(a,2)+pow(b,2))==pow(c,2)):
        retan = 'S'
    else:
        retan = 'N'
    print(tipo)
    print("Retangulo:",retan)
