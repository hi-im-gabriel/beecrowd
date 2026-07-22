a=input().split()
b=input().split()
cod1,qtde1,valor1=a
cod2,qtde2,valor2=b
tot=(int(qtde1)*float(valor1))+(int(qtde2)*float(valor2))
print("VALOR A PAGAR: R$ %.2f" % tot)
