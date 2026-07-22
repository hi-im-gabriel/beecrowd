a,b,c=map(float,input().split())
pi=3.14159
triangulo=(a*c)/2
circulo=pi*(c*c)
trapezio=c*(a+b)/2
quadrado=b*b
retangulo=a*b
print("TRIANGULO: %0.3f\nCIRCULO: %0.3f\nTRAPEZIO: %0.3f\nQUADRADO: %0.3f\nRETANGULO: %0.3f" % (triangulo, circulo, trapezio, quadrado, retangulo))
