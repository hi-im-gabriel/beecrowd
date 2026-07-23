#n=list(map(int,input().split()))
#s.pop() remover ultimo elemento
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfabeto
pi=3.1415
a,b=map(int,input().split())
a=a**3
aux=(4.0*(pi*a))/3.0
qt=0

while b>0:
    b-=aux
    qt+=1
print(qt-1)
