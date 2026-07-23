#n=list(map(int,input().split()))
#s.pop() remover ultimo elemento
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfa
def dividir(s):
    return [c for c in s]

def digito(f):
    i=b1=b2=0
    j=1
    while i<=8:
        b1+=int(f[i])*j
        i+=1
        j+=1
    i=0
    while i<=9:
        if i==9:
            b2+=int(b1)*i
        else:
            b2+=int(f[i])*i
        i+=1
    b1%=11
    b2%=11
    if b1==10:
        b1=0
    if b2==10:
        b2=0
    return b1,b2

while True:
    try:
        s=input()
        f=dividir(s)

        b1,b2=digito(f)
        print(f[0],f[1],f[2],sep="",end=".")
        print(f[3],f[4],f[5],sep="",end=".")
        print(f[6],f[7],f[8],sep="",end="-")
        print(b1,b2,sep="")
    except EOFError:
        break
