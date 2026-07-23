#n= list(map(int,input().split()))
#string.append(input()) array
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfabeto

def calc(sold,pulos):
    aux=0
    i=2
    while i<=sold:
        aux=(aux+pulos)%i
        i+=1
    return aux

n=int(input())
result=0
while n:
    sold,pulos=map(int,input().split())
    result+=1
    print("Case %d: %d" % (result,(calc(sold,pulos)+1)))
    n-=1
