for _ in range(int(input())):
    a,b,c=map(int,input().split())
    d=(b*b)-(4*a*c)
    v=-(d/(4.0*a))
    print(f"{v:.2f}")
