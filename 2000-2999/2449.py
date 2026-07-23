#n=list(map(int,input().split()))
#s.pop() remover ultimo elemento
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfa

while True:
    try:
        n,m=map(int,input().split())
        a=[0]*1124
        ans=dif=0
        aux=list(map(int,input().split()))
        for i in range(n):a[i]=aux[i]
        for i in range(n-1):
            dif=m-a[i]
            a[i]+=dif
            a[i+1]+=dif
            ans+=abs(dif)
        print(ans)  
    except EOFError:
        break
