n, c, t = map(int, input().split())
pipocas = list(map(int, input().split()))

inicio = (max(pipocas) + t - 1) // t
fim = (sum(pipocas) + t - 1) // t

while inicio < fim:
    meio = (inicio + fim) // 2
    capacidade = meio * t
    competidores = 1
    quantidade = 0

    for saco in pipocas:
        if quantidade + saco <= capacidade:
            quantidade += saco
        else:
            competidores += 1
            quantidade = saco

    if competidores <= c:
        fim = meio
    else:
        inicio = meio + 1

print(inicio)
