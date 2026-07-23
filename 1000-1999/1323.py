1
2
3
4
5
6
7
8
9
10
11
12
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
