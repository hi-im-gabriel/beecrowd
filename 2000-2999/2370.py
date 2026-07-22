n,t=map(int,input().split())
d=dict()
for i in range(n):
    nome,valor=input().split()
    d[nome]=int(valor)
d=dict(sorted(d.items(),key=lambda x: x[1],reverse=True))
f=list(d.keys())
aux=0
for i in range(t):
    print(f"Time {aux+1}")
    g=[]
    for i in range(aux,n,t):g.append(f[i])
    print(*sorted(g),sep="\n",end="\n\n")
    aux+=1
