def dif(x, y):
    q=[i for i in range(len(x)) if x[i]!=y[i]]
    return len(q)
e=str(input())
n=int(input())
v=[]
for i in range(5):v.append(dif(e, str(input())))
print(-1) if min(v) > n else print(f"{v.index(min(v))+1}\n{min(v)}")
