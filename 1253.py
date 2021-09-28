for i in range(int(input())):
    texto=input()
    qte=int(input())
    textonovo=''
    for l in texto:
        posicao=ord(l)-qte

        if posicao<65:textonovo+=chr(91-(65-posicao))
        else:textonovo+=chr(ord(l)-qte)
    print(textonovo)
