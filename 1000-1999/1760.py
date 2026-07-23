#n= list(map(int,input().split()))
#string.append(input()) array
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfabeto
from math import sqrt
while True:
    try:
        n=float(input())
        aux=float((sqrt(3)/4.00)*n*n)
        print("%.2f" % (aux*1.6))

    except EOFError:
        break
