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
