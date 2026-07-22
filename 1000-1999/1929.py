def res(a,b,c):
    if a>=b and a>=c:m,n,z=a,b,c
    else:
        if b>=c:m,n,z=b,a,c
        else:m,n,z=c,a,b
    if m>=n+z:return False
    return True
a,b,c,d=map(int,input().split())
print("S") if res(a,b,c) or res(a,b,d) or res(a,c,d) or res(b,c,d) else print("N")
