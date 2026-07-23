#n=list(map(int,input().split()))
#s.pop() remover ultimo elemento
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfa

def motoboy(pedidos, aux):
    entregas = []
    for x in range(len(pedidos) + 1):
        entregas.append([0 for x in range(aux + 1)])
    for pedido in range(1, len(pedidos) + 1):
        for ca in range(1, aux + 1):
            pedidoAtual = pedido - 1
            tempoEntrega = pedidos[pedidoAtual][0]
            quantPizza = pedidos[pedidoAtual][1]
            if quantPizza <= ca:
                if tempoEntrega + entregas[pedidoAtual][ca - quantPizza] > entregas[pedidoAtual][ca]:
                    entregas[pedido][ca] = tempoEntrega + entregas[pedidoAtual][ca - quantPizza]
                else:
                    entregas[pedido][ca] = entregas[pedidoAtual][ca]
            else:
                entregas[pedido][ca] = entregas[pedidoAtual][ca]
    tempo = entregas[len(pedidos)][aux]
    return tempo

while True:
    saasdasd=int(input())
    if saasdasd==0:
        break
    tempoEntrega = int(input())
    pedidos = []
    for x in range(saasdasd):
        p = input().split()
        p = (int(p[0]), int(p[1]))
        pedidos.append(p)
    pedidos.sort(reverse=True)
    res = motoboy(pedidos, tempoEntrega)
    print(res, "min.")
