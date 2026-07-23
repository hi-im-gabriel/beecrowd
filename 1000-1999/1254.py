1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
#n=list(map(int,input().split()))
#s.pop() remover ultimo elemento
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfa
while True:
    try:
        antigo = input().lower()
        novo = input()
        texto = input()
        palavras = texto.replace('<', '.<').replace('>', '>.').split('.')
        textoNovo = ""
        textoFinal = ""
        for palavra in palavras:
            novaPalavra = palavra
            if novaPalavra != '':
                if novaPalavra[0] == '<':
                    textoNovo += novaPalavra.lower().replace(antigo, novo)
                else:
                    textoNovo += novaPalavra
        palavras2 = texto.split(' ')
        palavras3 = textoNovo.split(' ')
        
        for nIndex in range(len(palavras3)):
            if palavras2[nIndex].lower() == palavras3[nIndex]:
                textoFinal += palavras2[nIndex] + ' '
            else:
                textoFinal += palavras3[nIndex] + ' '
        
        print(textoFinal[0:len(textoFinal) - 1])
    except EOFError:
        break
