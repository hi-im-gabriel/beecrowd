#n=list(map(int,input().split()))
#s.pop() remover ultimo elemento
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfa
n=[0]*1001
def res():
    n[0]=3
    n[1]=1
    i=2
    while i<=1000:
        qtd=2
        lim=i/2
        j=2
        while j<=lim:
            if i%j==0:
                qtd+=1
            j+=1
        n[i]=qtd
        i+=1

for c in range(int(input())):
    res()
    esferas=int(input())
    qtdpar=1
    i=3
    while i<=esferas:
        if n[i]%2==0:
            qtdpar+=1
        i+=1
    print(qtdpar)
