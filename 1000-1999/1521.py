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
#n=list(map(int,input().split()))
#s.pop() remover ultimo elemento
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfa
alunos=[0]*61
while True:
    n=int(input())
    if n==0:break
    aux=list(map(int,input().split()))
    i=1
    while i<=n:
        alunos[i]=aux[i-1]
        i+=1
    i=int(input())
    while alunos[i]!=i:
        i=alunos[i]
    print(i)
