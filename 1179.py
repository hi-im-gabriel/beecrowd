x=float(input())
n=[]
for i in range(100):
    n.append(x)
    x/=2
for i in range(100):print("N[%d] = %.4f"%(i,n[i]))
