1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
#n=list(map(int,input().split()))
#s.pop() remover ultimo elemento
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfabeto
import math
while True:
    try:
        n=int(input())
        h,c,l=input().split()
        aux=math.sqrt((int(c)**2)+(int(h)**2))
        aux*=(int(l)/100*int(n))/100
        print("%.4f"%aux)
    except EOFError:
        break
