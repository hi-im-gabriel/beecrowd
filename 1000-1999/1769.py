#n=list(map(int,input().split()))
#s.pop() remover ultimo elemento
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfa
def val(cpf):
    b1 = 0; b2 = 0
    mult1 = 1; mult2 = 9
    for d in cpf:
        b1 += mult1*int(d)
        b2 += mult2*int(d)
        mult1+=1; mult2-=1
    b1 = 0 if b1%11==10 else b1%11
    b2 = 0 if b2%11==10 else b2%11
    return  '{}{}'.format(b1, b2)

while True:
    try:
        line = input()
        first_part = line.split('-')[0].replace('.', '')
        second_part = line.split('-')[1]
        if val(first_part) == second_part:
            print('CPF valido')
            continue
        print('CPF invalido')
    except EOFError:
        break
