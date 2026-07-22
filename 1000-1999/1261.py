while True:
   try:
      n,m=map(int,input().split())
      d=dict()
      frase=""
      for i in range(n):
         s=input().split()
         d[s[0]]=int(s[1])
      for i in range(m):
         while True:
            aux=input()
            soma=0
            if aux==".":
               for i,j in d.items():
                  if i in frase:
                     soma+=(j*int(frase.count(i)))   
               print(soma)  
               frase=""
               break
            frase+=aux+" "
   except EOFError:break
