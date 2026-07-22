soma=0
for n in range(int(input())):
    horas,kmhora=map(int,input().split())
    soma+=(kmhora*horas)
print(soma)
