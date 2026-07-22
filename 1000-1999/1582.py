from math import gcd

def pita(x,y,z):
   if (x**2)+(y**2)==(z**2):return True
   return False

def primi(x,y,z):
   if gcd(gcd(x,y),z)==1:return True
   return False
while True:
   try:     
      x=list(map(int,input().split()))
      x.sort()
      if pita(x[0],x[1],x[2]):
         if primi(x[0],x[1],x[2]):
            print("tripla pitagorica primitiva")
         else:
            print("tripla pitagorica")
      else:
         print("tripla")
   except EOFError:break
