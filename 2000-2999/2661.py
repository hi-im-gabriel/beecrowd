n=int(input())
lim=2
fat=0
while lim*lim<=n:
   if n%lim==0:
      fat+=1
      while n%lim==0:
         n/=lim
   lim+=1
if n!=1:
   fat+=1
fat=(1<<fat)-fat-1
print(fat)
