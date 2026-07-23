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
    v=[0]*51
    aux=list(map(int,input().split()))
    for i in range(n):v[i]=aux[i]

    i=n-2
    while i>=0:
        j=n-1
        while j>i:
            v[i]+=v[j]
            j-=1
        i-=1
    soma=0
    for i in range(n):
        soma+=v[i]
    print(soma)
