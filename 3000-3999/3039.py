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
x = input()
x = int(x)
carrinhos=0
bonecas=0
while(x>=1):
    nome,sexo = input().split()
    if(sexo == 'F'):
        bonecas = bonecas + 1
    elif(sexo == 'M'):
        carrinhos = carrinhos + 1
    x = x - 1
print("%d carrinhos" % (carrinhos))
print("%d bonecas" % (bonecas))
