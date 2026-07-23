#n=list(map(int,input().split()))
#s.pop() remover ultimo elemento
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfa

n=list(map(int,input().split()))
ordenada=sorted(n)
reversaa=sorted(ordenada,reverse=True)
if n==ordenada:print('C')
elif n==reversaa:print('D')
else:print('N')
