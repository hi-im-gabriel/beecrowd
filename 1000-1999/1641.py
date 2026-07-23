#n=list(map(int,input().split()))
#s.pop() remover ultimo elemento
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfabeto
aux=1
while True:
    s=input().split()
    if len(s)==1:
        break
    r,x,y=s
    r=int(r)
    x=int(x)
    y=int(y)
    r=r*2
    if x*x+y*y<=r*r:
        print("Pizza %d fits on the table."%aux)
    else:
        print("Pizza %d does not fit on the table."%aux)
    aux+=1
