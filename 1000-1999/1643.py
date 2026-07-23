#n=list(map(int,input().split()))
#s.pop() remover ultimo elemento
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfa

fib=[0]*111
fib[1],fib[2]=1,2
for i in range(3,46):fib[i]=fib[i-1]+fib[i-2]
for i in range(int(input())):
    m=int(input())
    i=45
    aux=0
    while i>1:
        if fib[i]<=m:
            m-=fib[i]
            aux+=fib[i-1]
        i-=1
    print(aux)
