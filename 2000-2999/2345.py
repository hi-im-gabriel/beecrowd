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
#n= list(map(int,input().split()))
#string.append(input()) array
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfabeto
s = list(map(int,input().split()))
s=sorted(s)
result = abs((s[0] + s[3]) - (s[1] + s[2]))
print(result)
