pos=0
med=0.00
for i in range(6):
    x=float(input())
    if x>0:
        pos+=1
        med+=x
print(f"{pos} valores positivos")
print("%.1f"%(med/pos))
