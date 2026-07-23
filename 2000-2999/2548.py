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
#n=list(map(int,input().split()))
#s.pop() remover ultimo elemento
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfa
while True:
    try:
        l = []
        n,m=input().split()
        l = list(map(int,input().split()))
        aux = sum(l[int(n)-int(m):])
        print(aux)   
    except EOFError:
        break
