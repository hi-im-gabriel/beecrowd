#n=list(map(int,input().split()))
#string.append(input()) array
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfabeto
import string
alfa=list(string.ascii_lowercase)
n = int(input())
for nIndex in range(n):
    alfaValores = []
    valores = []
    texto = input().lower()
    maior = 1

    for caractere in texto:
        try:
            index = alfa.index(caractere)
            try:
                alfaValoresIndex = alfaValores.index(caractere)
                valores[alfaValoresIndex] += 1          
                if valores[alfaValoresIndex] > maior:
                    maior = valores[alfaValoresIndex]
            except ValueError:
                alfaValores.insert(len(alfaValores), caractere)
                valores.insert(len(valores), 1)
        except ValueError:
            continue
    
    maioresalfa = []

    for mIndex in range(len(valores)):
        if valores[mIndex] == maior:
            maioresalfa.insert(len(maioresalfa), alfaValores[mIndex])

    maioresalfa = sorted(maioresalfa)
    texto = ""

    for maiorLetra in maioresalfa:
        texto += maiorLetra

    print (texto)
