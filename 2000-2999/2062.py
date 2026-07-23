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
#n=list(map(int,input().split()))
#string.append(input()) array
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfabeto
n=int(input())
s=input().split()
f=[]
i=0
while i<=n-1:
    tam=len(s[i])
    if tam==3:
        if s[i][0]=='O' and s[i][1]=='B':
            f.append("OBI")
        elif s[i][0]=='U' and s[i][1]=='R':
            f.append("URI")
        else:
            f.append(s[i])
    else:
        f.append(s[i])
    i+=1
print(*f,sep=" ")
