def res(x,aux):
    aux1=0
    i=1
    while i<x:
        aux1=(aux1+aux)%i
        i+=1
    return aux1
while True:
    x=int(input())
    if x==0:break
    aux=1
    while res(x,aux)+2!=13:aux+=1
    print(aux)
