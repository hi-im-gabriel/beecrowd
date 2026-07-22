aux=n=0
med=0.00
while True:
    nota=float(input())
    if nota>10 or nota<0:print("nota invalida")
    else:
        aux+=1
        med+=nota
        if aux==2:
            print("media = %.2f"%(med/2))
            while True:
                print("novo calculo (1-sim 2-nao)")
                n=int(input())
                if n==1:
                    aux=n=0
                    med=0.00
                    break
                elif n==2:
                    break
    if n==2:break
