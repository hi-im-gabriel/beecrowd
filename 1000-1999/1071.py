x=int(input())
y=int(input())
menor=min(x,y)+1
maior=max(x,y)
if menor%2==0:menor+=1
soma=0
for i in range(menor,maior,2):soma+=i
print(soma)
