a=list(map(int,input().split()))
b=list(map(int,input().split()))
f=0
for i in range(3):
    if a[i]<b[i]:f+=(a[i]-b[i])
print(abs(f))
