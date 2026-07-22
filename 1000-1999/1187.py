t=input()
soma=aux=0
for i in range(12):
    for j in range(12):
        n=float(input())
        if (i==0 and j>0 and j<11)or(i==1 and j>1 and j<10)or(i==2 and j>2 and j<9)or(i==3 and j>3 and j<8)or(i==4 and j>4 and j<7):
            soma+=n
            aux+=1
print("%.1f"%soma) if t=="S" else print("%.1f"%(soma/aux))
