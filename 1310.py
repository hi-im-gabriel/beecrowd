def res(dia):
    max_menor = max_maior = dia[0]
    for i in dia[1:]:
        max_menor = max(i, max_menor + i)
        max_maior = max(max_maior, max_menor)
    return max_maior

while True:
    try:
        custo = int(input())
        dia = []
        for n in range(int(input())):dia.append(int(input()) - custo)
        aux = res(dia)
        if aux < 0:aux = 0
        print(aux)
    except EOFError:break
