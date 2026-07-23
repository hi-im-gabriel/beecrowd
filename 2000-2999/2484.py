#n=list(map(int,input().split()))
#s.pop() remover ultimo elemento
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfabeto
def sep(s):
    return [c for c in s]

while True:
    try:
        s=input()
        f=sep(s)
        print(*f,sep=" ")
        tam=len(f)
        aux=1
        for i in range(tam-1):
            f.pop()
            espaco=" "*aux
            print(espaco,end="")
            print(*f,sep=" ")
            aux+=1
        print()
    except EOFError:
        break
