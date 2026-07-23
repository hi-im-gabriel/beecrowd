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
#n=list(map(int,input().split()))
#string.append(input()) array
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfabeto
auxiliar=0
while True:
    n = int(input())
    s=[]
    if n==0:
        break
    for i in range(n):
        s.append(input())
    if auxiliar==1:
        print()
    maior=len(sorted(s,key=len)[n-1])
    i=0
    while i<=n-1:
        dif=maior-len(s[i])
        if dif!=0:
            j=1
            while j<=dif:
                print(" ",end="")
                j+=1
        print(s[i])
        i+=1
    auxiliar=1
