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
#alfa = list(string.ascii_lowercase) lsit do alfa
for i in range(int(input())):
    p1 = input()
    p2 = input()
    nome = ''
    for d in range(0, len(p1) - 1, 2):
        nome += p1[d:d+2] + p2[d:d+2]
    print(nome)
