a,b=map(int,input().split())
if a<0:
    e=abs(b)
    for r in range(e):
        f=a-r
        if f%b==0:break
    q=int(f/b)
else:
    q=int(a/b)
    r=int(a%abs(b))
print(q,r)
