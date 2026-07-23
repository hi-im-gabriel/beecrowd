#n=list(map(int,input().split()))
#s.pop() remover ultimo elemento
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfa
from math import sqrt
def res(x1,y1,x2,y2):
    return sqrt(pow(abs(x2 - x1), 2)+pow(abs(y2 - y1),2))

for i in range(int(input())):
    x1,y1,x2,y2,x3,y3=map(int,input().split())
    a=res(x1,y1,x2,y2)
    b=res(x2,y2,x3,y3)
    c=res(x3,y3,x1,y1)
    p=(a+b+c)/2
    area=sqrt(p * (p-a) * (p-b) * (p-c))
    print("%.3f"%area)
