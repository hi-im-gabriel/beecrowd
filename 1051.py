f=float(input())
if f<=2000.00:print("Isento")
else:
    if f>=2000.01 and f<=3000.00:aux=(f-2000.00)*0.08
    elif f>=3000.01 and f<=4500.00:aux=((f-3000.00)*0.18)+(999.99*0.08) 
    else:aux=((f-4500.00)*0.28)+(999.99*0.08)+(1499.99*0.18)
    print("R$ %.2f"%aux)
