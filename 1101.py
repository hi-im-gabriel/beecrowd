while True:
    x=input().split()
    soma=0
    if int(x[0]) <= 0 or int(x[1]) <= 0:
        break
    x=sorted(x)
    maior=int(x[1])
    menor=int(x[0])

    while menor <= maior:
        print(menor, end=' ')
        soma+=menor
        menor+=1
    print("Sum=%d" % soma)
