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
20
21
22
23
#n=list(map(int,input().split()))
#s.pop() remover ultimo elemento
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfabeto
def aux(a,b):
    r=int(a%b)
    if r==0:
        return int(b)
    return int(aux(b,r))
while True:
    try:
        x,y=map(int,input().split())
        mdc=int(aux(x,y))
        f=int(((x/mdc)*2)+((y/mdc)*2))
        print(f)
    except EOFError:
        break
