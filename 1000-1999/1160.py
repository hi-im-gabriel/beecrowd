for i in range(int(input())):
    popA,popB,gA,gB=map(float,input().split())
    aux=0
    while popA<=popB:
        popA+=int(((popA*gA)/100))
        popB+=int(((popB*gB)/100))
        aux+=1
        if aux>100:break
    print("Mais de 1 seculo.") if aux>100 else print(f"{aux} anos.")
