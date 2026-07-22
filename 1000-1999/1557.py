while True:
    m=[]
    n=1
    aux=0
    qtd=int(input())
    if qtd==0:break
    elif qtd==1:print(qtd)
    else:
        for i in range(qtd):
            linha=[]
            for l in range(qtd):
                linha.append(n)
                n=n * 2
            m.append(linha)
            n=m[aux][1]
            aux+=1
        tam=len(str(m[i][l]))
        for linha in m:
            for elemento in range(qtd):
                print('{:{}}' .format(linha[elemento],tam),end =' ') if elemento < qtd-1 else print('{:{}}' .format(linha[elemento],tam))
    print()
