a,b,c=map(float,input().split())
d=b*b-4*a*c
e=pow(d,.5)
if d<0 or a==0:print("Impossivel calcular")
else:
   f=(-b+e)/(2*a)
   g=(-b-e)/(2*a)
   print("R1 = %.5lf"%f)
   print("R2 = %.5lf"%g)
