for _ in range(int(input())):
    n,k=map(int,input().split())
    if k>n:r=n
    elif k==n:r=1
    else:r=int((n/k))+int((n%k))
    print(r)
