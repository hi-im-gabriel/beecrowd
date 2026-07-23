#n=list(map(int,input().split()))
#string.append(input()) array
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfabeto

n=int(input())
la,lb=map(int,input().split())
sa,sb=map(int,input().split())
if n>=la and n>=sa and n<=lb and n<=sb:
    print("possivel")
else:
    print("impossivel")
