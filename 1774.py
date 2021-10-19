def res(pai, i):
    if pai[i] == i:return i
    return res(pai, pai[i])
def juntar_g(pai, rank, x, y):
    raizDeX,raizDeY=res(pai,x),res(pai,y)
    if rank[raizDeX] < rank[raizDeY]:pai[raizDeX] = raizDeY
    elif rank[raizDeX] > rank[raizDeY]:pai[raizDeY] = raizDeX
    else:
        pai[raizDeY]=raizDeX
        rank[raizDeX]+=1
def custo_total(arestas,N):
    resultado=[]
    i=e=0
    arestas=sorted(arestas, key=lambda item:item[2])
    pai,rank=[],[]
    for no in range(N):
        pai.append(no)
        rank.append(0)
    while e < N-1:
        u,v,w = arestas[i]
        i += 1
        x,y= res(pai,u),res(pai,v)
        if x != y:
            e += 1 
            resultado.append([u,v,w])
            juntar_g(pai,rank,x,y)
    pesoTotal = 0
    for u,v,w in resultado:pesoTotal += w
    return pesoTotal
R,C = map(int,input().split())
arestas = []
for i in range(C):
    V,W,P = map(int, input().split())
    arestas.append([V-1,W-1,P])
print(custo_total(arestas,R))
