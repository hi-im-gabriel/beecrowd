#n=list(map(int,input().split()))
#string.append(input()) array
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfabeto
caso=1
for i in range(int(input())):
    med=0
    s=[]
    n=list(map(int,input().split()))
    tam=n[0]
    for i in range(1,tam+1):
        s.append(n[i])
    s=sorted(s)
    med=s[int(tam/2)]
    print("Case %d: %d"%(caso,med))
    caso+=1
