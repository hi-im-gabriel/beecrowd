t=input()
soma=aux=0
for i in range(12):
    for j in range(12):
        n=float(input())
        if i>=7 and i+j>=12 and j<i:
            soma+=n
            aux+=1
print("%.1f"%soma) if t=="S" else print("%.1f"%(soma/aux))
