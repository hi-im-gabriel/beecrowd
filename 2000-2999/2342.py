#n= list(map(int,input().split()))
#string.append(input()) array
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfabeto

n = int(input())
p = input().split()
if p[1] == '+':
    aux = int(p[0]) + int(p[2])
else:
    aux = int(p[0]) * int(p[2])

if aux > n:
    print("OVERFLOW")
else:
    print("OK")
