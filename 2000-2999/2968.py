#n= list(map(int,input().split()))
import math

a,b=input().split()
a=int(a)
b=int(b)

total=a*b

aux=[]

for i in range(1,10):
    perc=i/10
    qtd=total*perc
    qtd_str=str(math.ceil(qtd))
    aux.append(qtd_str)

res_str= " ".join(aux)

print(res_str)
