d=dict()
for i in range(int(input())):
    x=input().split()
    x[1],x[2],x[3]=int(x[1]),int(x[2]),int(x[3])
    d[i]=x
d=dict(sorted(d.items(),key=lambda x: x[1][0]))
d=dict(sorted(d.items(),key=lambda x: x[1][3]))
d=dict(sorted(d.items(),key=lambda x: x[1][2],reverse=True))
d=dict(sorted(d.items(),key=lambda x: x[1][1],reverse=True))
print(list(d.values())[0][0])
