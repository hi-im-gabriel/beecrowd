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
#n=list(map(int,input().split()))
#s.pop() remover ultimo elemento
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfabeto
n1,d1,v1 =map(int,input().split())
n2,d2,v2 =map(int,input().split())
t1=float(d1/v1)
t2=float(d2/v2)
if t1<t2:
    print(n1)
else:
    print(n2)
