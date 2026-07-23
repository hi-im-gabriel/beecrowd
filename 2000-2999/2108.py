#n=list(map(int,input().split()))
#s.pop() remover ultimo elemento
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfa
maior=""
while True:
    s=input().split()
    tam=len(s)
    if tam==1 and s[0]=='0':
        print()
        print("The biggest word: %s"%maior)
        break
    f=[]
    for i in range(tam):
        aux=len(s[i])
        f.append(s[i])
        if i!=tam-1:
            print("%d-"%aux,end="")
        else:
            print("%d"%aux)
    f=sorted(f,key=len)
    if len(f[tam-1])>=len(maior):
        maior=f[tam-1]
