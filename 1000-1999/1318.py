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
while True:
    try:
        a,b = map(int, input().split())
        if a==0 and b==0:
            break
        l = list(map(int,input().split()))
        l1 = l.copy()
        l1 = set(l1)
        res = 0
        for i in l1:
            if i in l:
               if l.count(i) >= 2:
                   res += 1
        print(res)
    except EOFError:
        break
