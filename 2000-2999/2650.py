def ltos(s):
   f=""
   aux=False
   for c in s:
      if aux:f+=" "
      f+=c
      aux=True
   return f
n,w=map(int,input().split())
f=[]
for i in range(n):
   s=input().split()
   x=int(s.pop(-1))
   s=ltos(s)
   if x>w:
      f.append(s)
print(*f,sep="\n")
