#n= list(map(int,input().split()))
#string.append(input()) array
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfabeto

nota = {'W' : 1, 'H' : 1/2, 'Q' : 1/4, 'E' : 1/8, 'S' : 1/16, 'T' : 1/32, 'X' : 1/64}
while True:
    c = input()
    if c == '*':
        break
    c = [x for x in c.split('/') if x]
    aux = 0

    for conjunto in c:
        dur = 0
        for iden in conjunto:
            dur += nota[iden]
            if dur > 1:
                break
        if dur == 1:
            aux += 1

    print(aux)
