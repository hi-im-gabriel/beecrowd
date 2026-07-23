#n= list(map(int,input().split()))
#string.append(input()) array
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfabeto

for i in range(int(input())):
    t=int(input())
    aux=0
    altura=list(map(int,input().split()))
    pulos=input()
    j=0
    while j<t:
        if pulos[j]=='S':
            if altura[j]<3:
                aux+=1
        else:
            if altura[j]>2:
                aux+=1
        j+=1
    print(aux)
