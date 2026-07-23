#n= list(map(int,input().split()))
#string.append(input()) array
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfabeto

while True:
    n=int(input())
    aux=0.00
    if n==0:
        break
    i=1
    while i<=n:
        q,a,b=map(float,input().split())
        print("Size #%d:" % i)
        aux=float((((a+b)*5.00)/2)*q)
        print("Ice Cream Used: %.2lf cm2" % aux)
        i+=1
    print()
