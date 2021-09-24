int(input())
x=list(map(int,input().split()))
print(f"Menor valor: {min(x)}\nPosicao: {x.index(min(x))}")
