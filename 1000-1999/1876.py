#n= list(map(int,input().split()))
#string.append(input()) array
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfabeto

while True:
    try:
        s=input()
        result=aux=maximus=0
        i=0
        while i<len(s):
            if s[i] != 'x':
                aux+=1
            else:
                if result==0:
                    maximus=max(maximus,aux)
                    result=1
                else:
                    maximus=max(maximus,aux/2)
                aux=0

            i+=1
        maximus=int(max(maximus,aux))
        print(maximus)

    except EOFError:
        break
