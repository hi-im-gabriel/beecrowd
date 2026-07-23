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
33
34
35
36
37
38
39
40
41
42
43
44
45
#n=list(map(int,input().split()))
#s.pop() remover ultimo elemento
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfa
def dividir(s):
    return [c for c in s]
def digito(f):
    i=b1=b2=0
    j=1
    while i<=8:
        b1+=int(f[i])*j
        i+=1
        j+=1
    i=0
    while i<=9:
        if i==9:
            b2+=int(b1)*i
        else:
            b2+=int(f[i])*i
        i+=1
    b1%=11
    b2%=11
    if b1==10:
        b1=0
    if b2==10:
        b2=0
    return b1,b2
while True:
    try:
        s=input()
        f=dividir(s)
        b1,b2=digito(f)
        print(f[0],f[1],f[2],sep="",end=".")
        print(f[3],f[4],f[5],sep="",end=".")
        print(f[6],f[7],f[8],sep="",end="-")
        print(b1,b2,sep="")
    except EOFError:
        break
