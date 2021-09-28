while True:
    n=int(input())
    if n==0:break
    x=list(map(int,input().split()))
    print(f"Mary won {x.count(0)} times and John won {x.count(1)} times")
