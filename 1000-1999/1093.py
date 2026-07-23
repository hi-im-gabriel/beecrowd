#n=list(map(int,input().split()))
#s.pop() remover ultimo elemento
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfa

from math import ceil
lados = 6

while True:
    ev1,ev2,at,d=map(int,input().split())

    if ev1==ev2==at==d==0:
        break
    v1,v2=ceil(ev1/d),ceil(ev2/d)
    if at==3:
        aux=v1/(v1+v2)*100
        print("%.1f"%(aux))
    else:
        dado = 1 - (lados - at)/lados
        dado = (1 - dado)/dado
        aux = (1 - pow(dado, v1))/(1 - pow(dado, v1+v2)) * 100
        print("%.1f"%(aux))
