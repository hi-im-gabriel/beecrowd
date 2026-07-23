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
24
25
26
27
28
29
30
31
32
#n=list(map(int,input().split()))
#s.pop() remover ultimo elemento
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfa
caso=1
testando=0
while True:
    try:
        iguais=fem=mas=0
        n=int(input())
        s=input().split()
        tam=len(s)
        if testando>0:print()
        for i in range(0,tam,2):
            if int(s[i])==n:
                iguais+=1
                if s[i+1]=='M':
                    mas+=1
                elif s[i+1]=='F':
                    fem+=1
        print(f"Caso {caso}:")
        print(f"Pares Iguais: {iguais}")
        print(f"F: {fem}")
        print(f"M: {mas}")
        caso+=1
        testando+=1
    except EOFError:
        break
