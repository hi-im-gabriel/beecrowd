n=int(input())
x=sorted(list(map(int,input().split())),reverse=True)
tot=sum(x)
d=dict()
for i in x:d[i]=(100*i)/tot
ver=list(d.values())[1]
for i,j in d.items():
    if i>x[1]:
        if j>=45.00:print(1)
        elif j>=40.00 and j-ver>10.00:print(1)
        else:print(2)
    else:print(2)
    break
