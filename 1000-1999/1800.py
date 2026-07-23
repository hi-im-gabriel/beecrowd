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
#n=list(map(int,input().split()))
#s.pop() remover ultimo elemento
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfa
vetor=[0]*1101
while True:
    try:
        q,e=map(int,input().split())
        
        s=list(map(int,input().split()))
        for i in range(e):
            vetor[s[i]]=s[i]
        for i in range (q):
            tmp=int(input())
            if tmp==vetor[tmp]:
                print("0")
            else:
                print("1")
                vetor[tmp]=tmp
    except EOFError:
        break
