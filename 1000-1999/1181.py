m=[[0]*13]*13
l=int(input())
t=input()
op=0.00
for x in range(12):
    for y in range(12):
        m[x][y]=float(input())
        if x==l:op+=m[x][y]
if t=='S':print("%.1f"%op)
else:print("%.1f"%(op/12.0))
