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
#n=list(map(int,input().split()))
#s.pop() remover ultimo elemento
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfa
def res(n):
    if not n%2:return int(n/2)
    return int(n/2+1)
for _ in range(int(input())):
    print(res(int(input())))
