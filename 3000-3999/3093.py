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
#n= list(map(int,input().split()))
#string.append(input()) array
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
n=int(input())
while n:
    s=input().split()
    if s[0].count('Q')>=1 and s[0].count('J')>=1 and s[0].count('K')>=1 and s[0].count('A')>=1:
        print("Aaah muleke")
    else:
        print("Ooo raca viu")
    n-=1
