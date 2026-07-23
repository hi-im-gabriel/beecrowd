#n=list(map(int,input().split()))
#s.pop() remover ultimo elemento
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfabeto

fat=[1,2,6,24,120,720,5040,40320]
n=int(input())
x=0
i=7
while i>=0:
    x+=int(n/fat[i])
    n%=int(fat[i])
    i-=1
print(int(x))
