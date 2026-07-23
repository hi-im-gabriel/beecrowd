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
f=[]
carros,voltas=map(int,input().split())
for i in range(carros):
    f.append(sum(list(map(int,input().split()))))
ord=sorted(f)
for i in range (3):
    print(f.index(ord[i])+1)
