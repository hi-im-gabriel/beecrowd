n,k=map(int,input().split())
r=list(map(int,input().split()))
x=[0 for x in range(k)]
for i in r:x[i-1] +=1
print(min(x))
