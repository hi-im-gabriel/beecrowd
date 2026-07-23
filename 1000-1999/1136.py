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
#alfa = list(string.ascii_lowercase) lsit do alfa
def res(n,b,f):
    s=set()
    for i in range(b):
        for j in range(i+1,b):
            s.add(abs(f[i]-f[j]))
    for i in range(1,n+1):
        if not i in s:
            return "N"
    return "Y"
while True:
    n,b=map(int,input().split())
    if n==b==0:break
    f=list(map(int,input().split()))
    print(res(n,b,f))
