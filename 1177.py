n=int(input())
aux=0
x=[]
for i in range(1000):
    x.append(aux)
    aux+=1
    if aux>=n:aux=0
for i in range(1000):print(f"N[{i}] = {x[i]}")
