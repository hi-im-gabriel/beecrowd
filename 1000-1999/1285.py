#n=list(map(int,input().split()))
#string.append(input()) array
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfabeto
while True:
    try:
        n,m=input().split()
        aux=0
        for x in range(int(n), int(m)+1):
            if len(set(list(str(x)))) == len(str(x)):
                aux += 1
        print(aux)          
    except EOFError:
        break
