for _ in range(int(input())):
    a,b=map(int,input().split())
    if b==0:print("divisao impossivel")
    else:print("%.1f"%(a/b))
