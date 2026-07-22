while True:
    n=int(input())
    if n==0:break
    if n%2!=0:n+=1
    a=[x for x in range(n,n+9,2)]
    print(sum(a))
