#n=list(map(int,input().split()))
#string.append(input()) array
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfabeto

for i in range(int(input())):
    s=input()
    f=[]
    tam=len(s)-1
    j=0
    while j<=tam:
        if s[tam].islower():
            f.append(s[tam])
        tam-=1
    print(*f,sep="")
