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
#d=dict()
#d[key]=s[value]
#d=dict(sorted(d.items(), key=lambda item: item[1]))
def dist(x,y,a,b):
    return abs(x-a)+abs(y-b)
x,y,a,b=map(int,input().split())
print(dist(x,y,a,b))
