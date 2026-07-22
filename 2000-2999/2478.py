n=int(input())
d=dict()
sim="Uhul! Seu amigo secreto vai adorar o/"
nao="Tente Novamente!"
for i in range(n):
    nome,p1,p2,p3=input().split()
    d[nome]=[p1,p2,p3]
while True:
    try:
        nome,p=input().split()
        try:
            print(sim) if p in d.get(nome) else print(nao)
        except:print(nao)
    except EOFError:break
