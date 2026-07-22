aux=False
while True:
    n=int(input())
    if n==0:break
    d=dict()
    for i in range(n):
        nome=input()
        x=input().split()
        x.append(nome)
        d[i]=x
    d=dict(sorted(d.items(),key=lambda x: x[1][2]))
    d=dict(sorted(d.items(),key=lambda x: x[1][1],reverse=True))
    d=dict(sorted(d.items(),key=lambda x: x[1][0]))
    if aux:print()
    for i,j in d.items():
        print(*j,sep=" ")
    aux=True
