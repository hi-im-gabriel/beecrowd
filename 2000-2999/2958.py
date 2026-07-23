#n= list(map(int,input().split()))
#string.append(input()) array
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfabeto

linhas,colunas=map(int,input().split())
v=[]
d=[]
for i in range(linhas):
    scan=input().split()
    for i in range(colunas):
        if scan[i][1]=='V':
            v.append(scan[i])
        else:
            d.append(scan[i])
v=sorted(v,reverse=True)
d=sorted(d,reverse=True)
print(*v,sep="\n")
print(*d,sep="\n")
