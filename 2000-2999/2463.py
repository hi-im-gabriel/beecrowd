n=int(input())
a=list(map(int,input().split()))
soma=aux=0
for i in a:
   soma+=i
   aux=max(aux,soma)
   if soma<0:soma=0
print(aux)
