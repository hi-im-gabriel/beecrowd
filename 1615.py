for _ in range(int(input())):
   n,m=map(int,input().split())
   d=dict()
   x=list(map(int,input().split()))
   for i in range(1,n+1):
      d[i]=x.count(i)
   d=dict(sorted(d.items(),key=lambda item: item[1],reverse=True))
   a=list(d.values())
   b=list(d.keys())
   print(b[0]) if (a[0]>int(len(x)/2) and a[0]>a[1]) else print(-1)
