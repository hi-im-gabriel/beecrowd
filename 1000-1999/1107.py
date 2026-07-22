while True:
    altura, comprimento = map(int, input().split())
    if altura == comprimento == 0:
        break
    x = list(map(int, input().split()))
    quant = 0
    xant = 0
    for i in range(len(x)):
        if i == 0:
            quant += altura - x[i]
        elif x[i] < xant:
            quant += xant - x[i]
        xant = x[i]
    print(quant)
