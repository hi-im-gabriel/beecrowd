aux=med=0
while True:
    f=float(input())
    if f<0 or f>10:print("nota invalida")
    else:
        aux+=1
        med+=f
    if aux==2:break
print("media = %.2f"%(med/2))
