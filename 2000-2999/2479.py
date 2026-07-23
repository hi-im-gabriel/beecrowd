#n= list(map(int,input().split()))
#string.append(input()) array
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)

n=int(input())
names=[]
sim=nao=0
while n:
    op,nome=input().split()
    names.append(nome)
    if op=='+':
        sim+=1
    else:
        nao+=1
    n-=1
names=sorted(names)
print(*names,sep="\n")
print("Se comportaram: %d | Nao se comportaram: %d" % (sim,nao))
