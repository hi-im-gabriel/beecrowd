while True:
    n=int(input())
    if n==0:break
    n=[x for x in range(1,n+1)]
    print(*n,sep=" ")
