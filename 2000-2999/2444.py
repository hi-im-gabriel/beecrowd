#n= list(map(int,input().split()))
#string.append(input()) array
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfabeto

ini,ntrocas=map(int,input().split())
s=list(map(int,input().split()))
tam=len(s)
aux=0
for i in range(tam):
    if ini+s[i]>100:
        ini=100
    elif ini+s[i]>0:
        ini+=s[i]
    else:
        ini=0
print(ini)
