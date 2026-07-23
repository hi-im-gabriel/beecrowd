#n=list(map(int,input().split()))
#string.append(input()) array
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfabeto
aux=cont=0
while True:
    try:
        nome=input()
        dist=int(input())
        aux+=dist
        cont+=1
    except EOFError:
        print("%.1lf" % (aux/cont))
        break
