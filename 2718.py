for i in range(int(input())):
    x=bin(int(input()))
    x=x[2:]
    m=0
    aux=0
    for i in x:
        if i == '1':aux+=1
        else:aux=0
        if aux > m:m=aux
    print(m)
