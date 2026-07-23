#n=list(map(int,input().split()))
#s.pop() remover ultimo elemento
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfa

turma = 1
while True:
    n =int(input())
    if n==0:
        break
    c = []
    while n:
        n -= 1
        c.append([int(x) for x in input().split()])

    maior = max([x[1] for x in c])
    estagio = [str(x[0]) for x in c if x[1] == maior]

    print('Turma %d' % turma)
    print(' '.join(estagio), '')
    print()
    turma += 1
