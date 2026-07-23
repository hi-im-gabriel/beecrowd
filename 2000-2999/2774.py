#n= list(map(int,input().split()))
#string.append(input()) array
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfabeto

from math import sqrt

def calc(qt, lista, media):
    result = 0
    for caso in range(qt):
        result += (lista[caso] - media)**2
    final = sqrt( (result) / (qt - 1) )
    return final
while True:
    try:
        h, m = input().split()
        medidas = [float(x) for x in input().split()]
        casos = (int(h) * 60) // int(m)
        media = sum(medidas) / casos
        final = calc(casos, medidas, media)
        print('%.5f' % final)
    except EOFError:
        break
