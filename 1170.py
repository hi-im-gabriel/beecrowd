for n in range(int(input())):
    c=float(input())
    aux=0
    while c>1:
        c/=2
        aux+=1
    print(f"{aux} dias")
    aux=0
