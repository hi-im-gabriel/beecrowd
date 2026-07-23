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
#n= list(map(int,input().split()))
#string.append(input()) array
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
t=int(input())
if t==1:
    print("Top 1")
elif t>1 and t<=3:
    print("Top 3")
elif t>3 and t<=5:
    print("Top 5")
elif t>5 and t<=10:
    print("Top 10")
elif t>10 and t<=25:
    print("Top 25")
elif t>25 and t<=50:
    print("Top 50")
elif t>50 and t<=100:
    print("Top 100")
