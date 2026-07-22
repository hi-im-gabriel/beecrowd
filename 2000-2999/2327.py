def magico(mat) :
   n = len(mat)
   sumd1=sumd2=0
   for i in range(n):
      sumd1+=mat[i][i]
      sumd2+=mat[i][n-i-1]
   if not(sumd1==sumd2):return False
   for i in range(n):
      sumr=0
      sumc=0
      for j in range(n):
         sumr+=mat[i][j]
         sumc+=mat[j][i]
      if not(sumr==sumc==sumd1):return False
   return True
n=int(input())
matriz=[]
for i in range(n):
   x=list(map(int,input().split()))
   matriz.append(x)
print(sum(x)) if magico(matriz) else print(-1)
