par=impar=pos=neg=0
for i in range(5):
    n=int(input())
    if n%2==0:par+=1
    else:impar+=1
    if n>0:pos+=1
    elif n<0:neg+=1
print(f"{par} valor(es) par(es)\n{impar} valor(es) impar(es)\n{pos} valor(es) positivo(s)\n{neg} valor(es) negativo(s)")
