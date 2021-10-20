n=int(input())
v=list(map(int,input().split()))
f=[]
for i in range(1, n): f.append(v[i]-v[i-1])
aux=[x for x in range(1,n-1) if f[x]!=f[x-1]]
print(len(aux)+1)
