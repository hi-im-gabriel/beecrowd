n=float(input())
if n<=400.00:
    novo=n*1.15
    perc=15
elif n>=400.01 and n<=800.00:
    novo=n*1.12
    perc=12
elif n>=800.01 and n<=1200.00:
    novo=n*1.10
    perc=10
elif n>=1200.01 and n<=2000.00:
    novo=n*1.07
    perc=7
else:
    novo=n*1.04
    perc=4
reaj=novo-n
print("Novo salario: %.2f"%novo)
print("Reajuste ganho: %.2f"%reaj)
print(f"Em percentual: {perc} %")
