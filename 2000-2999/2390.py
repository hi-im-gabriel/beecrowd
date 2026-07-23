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
#n=list(map(int,input().split()))
#s.pop() remover ultimo elemento
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfa
aux=aux1=-1
tempo=0
for i in range(int(input())):
    n=int(input())
    if aux != aux1 and n-aux<10:
        tempo-=10-(n-aux)
    aux=n
    tempo+=10
print(tempo)
