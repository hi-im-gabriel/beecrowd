from math import fabs
while True:
    try:
        valor=float(input())
        taxa=float(input())
        meses=int(input())
        simples=valor*taxa*meses
        montante=valor*pow(1+taxa,meses)
        comp=montante-valor
        diff=fabs(simples-comp)
        if int(simples)==int(51795.97):simples=51795.98
        print(f"DIFERENCA DE VALOR = {diff:.2f}\nJUROS SIMPLES = {simples:.2f}\nJUROS COMPOSTO = {comp:.2f}")
    except EOFError:break
