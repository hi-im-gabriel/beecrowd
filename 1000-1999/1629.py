#n=list(map(int,input().split()))
#s.pop() remover ultimo elemento
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfa

while True:
    n = int(input())
    if n == 0:
        break
    while n > 0:
        n -= 1
        um = 0
        zero = 0
        linha = input()
        for i in range(len(linha)):
            if i % 2 == 0:
                zero += int(linha[i])
            else:
                um += int(linha[i])
        resultado = 0
        while (zero):
            resultado += (zero % 10)
            zero = int(zero/10)
        while (um):
            resultado += (um % 10)
            um = int(um/10)
        print(resultado)
