while True:
   n=int(input())
   if n==0:break
   a=0
   while n>1:
      if n%3==0:
         a+=int(n/3)
         n/=3
         n=int(n)
      else:
         a+=int((n/3))+1
         n=int((n/3))+1
   print(a)
