#n= list(map(int,input().split()))
#string.append(input()) array
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfabeto
from math import sqrt

n = int(input())
primo = []
for i in range(n, 64000):
    p = 1
    for j in range(2, int(sqrt(i)) + 1 ):
        if i % j == 0:
            p = 0
            break
    if p:
        primo.append(i)
    if len(primo) == 10:
        break
vel = sum(primo)
print(vel, 'km/h')
h = int(60000000/vel)
d = int(h/24)
print(h, 'h /', d, 'd')
