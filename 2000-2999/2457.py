#n=list(map(int,input().split()))
#s.pop() remover ultimo elemento
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfa

c=input()
s=input().split()
tam=len(s)
aux=i=0
for i in range(tam):
    if c in s[i]:
        aux+=1
x=float((aux/tam)*100)
print("%.1f"%x)
