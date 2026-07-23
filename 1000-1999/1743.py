#n=list(map(int,input().split()))
#string.append(input()) array
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfabeto

def encaixe(m,f):
    i=j=0
    while i<5:
        if m[i]==f[i]:
            return False
        i+=1
        j+=1
    return True

m=list(map(int,input().split()))
f=list(map(int,input().split()))
if encaixe(m,f):
    print("Y")
else:
    print("N")
