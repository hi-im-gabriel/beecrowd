a,b,c=map(float,input().split())
if a<b+c and b<c+c and c<a+b:print("Perimetro = %.1lf"%(a+b+c))
else:print("Area = %.1lf"%((a+b)*c/2))
