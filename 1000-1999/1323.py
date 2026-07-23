#n= list(map(int,input().split()))

while True:
    n=int(input())
    if n==0:
        break
    tot=0
    while n:
        tot+=(n*n)

        n-=1
    print(tot)
