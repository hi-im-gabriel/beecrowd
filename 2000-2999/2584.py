from math import tan
for c in range(int(input())):
   n=int(input())
   alt=(n/(2*tan((36*3.14159265358979323846)/180)))
   area=(10*((n*alt)/4))
   print("%.3f"%area)
