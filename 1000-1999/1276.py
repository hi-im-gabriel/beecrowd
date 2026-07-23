#n=list(map(int,input().split()))
#s.pop() remover ultimo elemento
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfa
import string
alfa = list(string.ascii_lowercase)

while True:
    try:
        texto = input().replace(' ', '')
        letras = []

        for letra in texto:
            try:
                letras.index(letra)
            except ValueError:
                letras.insert(len(letras), letra)
        
        faixas = []
        letras = sorted(letras)
        primeiraLetra = ''
        ultimaLetra = ''
        
        for letra in letras:
            if primeiraLetra == '':
                primeiraLetra = letra
                ultimaLetra = letra
            else:
                if alfa.index(letra) == alfa.index(ultimaLetra) + 1:
                    ultimaLetra = letra
                else:
                    faixas.insert(len(faixas), primeiraLetra + ':' + ultimaLetra)
                    primeiraLetra = letra
                    ultimaLetra = letra
        
        if primeiraLetra and ultimaLetra:
            faixas.insert(len(faixas), primeiraLetra + ':' + ultimaLetra)
        elif primeiraLetra and ultimaLetra == '':
            faixas.insert(len(faixas), primeiraLetra + ':' + ultimaLetra)
        
        textoFinal = ''

        for faixa in faixas:
            textoFinal += faixa + ", "
        
        print (textoFinal[0: len(textoFinal) - 2])
    except EOFError:
        break
