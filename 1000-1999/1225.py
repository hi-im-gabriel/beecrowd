#n=list(map(int,input().split()))
#s.pop() remover ultimo elemento
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfa
def res(vet,s,l):
    if s%l!=0:return -1
    maior=0
    s=s/l
    for i in range(l):
        if vet[i]>s:
            maior+=vet[i]-s
    return int(maior+1)

while True:
    try:
        n=int(input())
        vet=[0]*(n+1)
        aux=list(map(int,input().split()))
        soma=0
        for i in range(n):vet[i]=aux[i]
        for i in range(n):
            soma+=vet[i]
        print(res(vet,soma,n))
    except EOFError:
        break
