while True:
    n,k=map(int,input().split())
    if n==0==k:break
    p = list(map(int,input().split()))
    total = 0
    for i in set(p):
        if p.count(i) >= k:total += 1
    print(total)
