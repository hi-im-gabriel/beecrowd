t=input()
m=[]
for i in range(12):
    for j in range(12):
        n=float(input())
        if i<j:m.append(n)
print(("%.1f")%(sum(m))) if t=="S" else print(("%.1f")%(sum(m)/len(m)))
