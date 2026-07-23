#n=list(map(int,input().split()))
#s.pop() remover ultimo elemento
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfa

while True:
    n=int(input())
    if n==0:break
    aux=n
    while n!=1:
        if n%2==0:
            aux1=0.5*n
        else:
            aux1=3*n+1
        if aux1>aux:
            aux=aux1
        n=aux1
    print(int(aux))
