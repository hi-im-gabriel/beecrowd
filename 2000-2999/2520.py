from math import sqrt
def dist(x1,y1,x2,y2):
   return int(sqrt(pow(x2-x1,2)+pow(y2-y1,2)*1.0))
while True:
   try:
      n,m=map(int,input().split())
      f=[[0]*m]*n
      linha_um=linha_dois=coluna_um=coluna_dois=0
      for i in range(n):
         s=list(map(int,input().split()))
         f[i]=s
         for j in range(m):
            if s[j]==2:
               linha_dois=i
               coluna_dois=j
            elif s[j]==1:
               linha_um=i
               coluna_um=j
      print(abs(linha_um-linha_dois)+abs(coluna_dois-coluna_um))
   except EOFError:break
