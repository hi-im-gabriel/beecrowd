def sacoPapaiNoel(itens, capacidade=50):
    sacos = []
    for x in range(len(itens) + 1):sacos.append([[0, 50, len(itens)] for x in range(capacidade + 1)])
    for item in range(1, len(itens) + 1):
        for p in range(1, capacidade + 1):
            itemAtual = item - 1
            quantBri = itens[itemAtual][0]
            pesoBri = itens[itemAtual][1]
            if pesoBri <= p:
                if quantBri + sacos[itemAtual][p - pesoBri][0] > sacos[itemAtual][p][0]:
                    sacos[item][p][0] = quantBri + sacos[itemAtual][p - pesoBri][0]
                    sacos[item][p][1] = sacos[itemAtual][p - pesoBri][1] - pesoBri
                    sacos[item][p][2] = sacos[itemAtual][p - pesoBri][2] - 1
                else:sacos[item][p] = sacos[itemAtual][p]
            else:sacos[item][p] = sacos[itemAtual][p]
    res = sacos[len(itens)][capacidade]
    return res[0], 50 - res[1], res[2]
for _ in range(int(input())):
    conjuntosBrinquedos=int(input())
    conjuntos=[]
    for _ in range(conjuntosBrinquedos):
        quantB, pesoB =map(int,input().split())
        conjunto=(quantB, pesoB)
        conjuntos.append(conjunto)
    brinquedos, peso, sobra = sacoPapaiNoel(conjuntos)
    print(f"{brinquedos} brinquedos\nPeso: {peso} kg\nsobra(m) {sobra} pacote(s)\n")
