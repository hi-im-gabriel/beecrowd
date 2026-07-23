#n=list(map(int,input().split()))
#s.pop() remover ultimo elemento
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfabeto

n=int(input())
aux=7
if n>=101:
    aux+=(n-100)*5+160
elif n>=31:
    aux+=(n-30)*2+20
elif n>=11:
    aux+=n-10
print(aux)
