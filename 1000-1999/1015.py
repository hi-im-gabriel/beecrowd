from math import sqrt
x1,y1=map(float,input().split())
x2,y2=map(float,input().split())
p1=x2-x1
p2=y2-y1
res=sqrt((p1*p1)+(p2*p2))
print("%.4f"%res)
