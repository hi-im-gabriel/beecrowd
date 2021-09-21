def imp(x):
   return [c for c in x if c%2!=0]

for _ in range(int(input())):
   n=int(input())
   x=imp(list(map(int,input().split())))
   xM=sorted(x,reverse=True)
   xN=sorted(x)
   tam=len(x)
   f=[]
   if tam==0:tam=0
   else:
      for i in range(int(tam/2)):
         f.append(xM[i])
         f.append(xN[i])
   if tam%2!=0:f.append(xM[int(tam/2)])
   print() if tam==0 else print(*f,sep=" ")
