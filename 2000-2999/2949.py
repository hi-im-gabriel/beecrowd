#n=list(map(int,input().split()))
#s.pop() remover ultimo elemento
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfabeto
a=e=h=m=x=0
for i in range(int(input())):
    nome,tipo=input().split()
    if tipo=='A':
        a+=1
    elif tipo=='E':
        e+=1
    elif tipo =='H':
        h+=1
    elif tipo =='M':
        m+=1
    elif tipo =='X':
        x+=1
print("%d Hobbit(s)"%x)
print("%d Humano(s)"%h)
print("%d Elfo(s)"%e)
print("%d Anao(s)"%a)
print("%d Mago(s)"%m)
