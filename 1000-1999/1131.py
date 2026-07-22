inter=gremio=empate=0
while True:
    i,g=map(int,input().split())
    if i>g:inter+=1
    elif g>i:gremio+=1
    else:empate+=1
    print("Novo grenal (1-sim 2-nao)")
    n=int(input())
    if n==2:break
print(f"{inter+gremio+empate} grenais\nInter:{inter}\nGremio:{gremio}\nEmpates:{empate}")
if i>g:print("Inter venceu mais")
elif g>i:print("Gremio venceu mais")
else:print("Nao houve vencedor")
