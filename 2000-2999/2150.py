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
        s=input()
        f=input()
        tam=len(s)
        aux=aux1=0
        for i in range(tam):
            aux1=f.count(s[i])
            if aux1>0:
                aux+=aux1
        print(aux)
    except EOFError:
        break
