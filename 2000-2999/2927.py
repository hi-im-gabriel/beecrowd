#n=list(map(int,input().split()))
#string.append(input()) array
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfabeto
nalunos,npc,qtpcq,qtpcs=map(int,input().split())
if npc-qtpcq-qtpcs>nalunos:
    print("Igor feliz!")
else:
    if qtpcq>qtpcs/2:
        print("Caio, a culpa eh sua!")
    else:
        print("Igor bolado!")
