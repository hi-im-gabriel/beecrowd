f=[0]*100003
f[3]=1
i=4
while i<=100000:
    f[i]=(i*f[i-1])%1000000009
    i+=1
while True:
    n=int(input())
    if n==0:break
    print(f[n])
