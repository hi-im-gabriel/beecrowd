#n=list(map(int,input().split()))
#s.pop() remover ultimo elemento
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfa
vogais=['a','e','i','o','u']
termina1=['o','s','x']
termina2=['c','h','s']
singular=""
plural=""
l,n=map(int,input().split())
for i in range(l):
    x=input().split()
    singular+=x[0]+' '
    plural+=x[1]+' '
singular=list(singular.split())
plural=list(plural.split())
for i in range(n):
    x=input()
    if x in singular:
        print(plural[singular.index(x)])
    else:
        tam=len(x)-1
        if x[tam-1] not in vogais and x[tam]=='y':
            x=x.replace('y',"ies")
        elif (x[tam] in termina1) or (x[tam] in termina2 and x[tam-1] in termina2):
            x+='es' 
        else:
            x+='s'
        print(x)
