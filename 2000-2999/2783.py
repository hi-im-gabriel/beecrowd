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
#import string
#alfa = list(string.ascii_lowercase) lsit do alfabeto
e = input()
figurinha = [int(x) for x in str(input()).split()]
l = [int(x) for x in str(input()).split()]
aux = 0
for i in figurinha:
    if not i in l: aux += 1
print(aux)
