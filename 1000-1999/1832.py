import string
maiusculo=list(string.ascii_uppercase)
minusculo=list(string.ascii_lowercase)
res_maiusculo=[193,194,195,196,197,198,199,200,201,209,210,211,212,213,214,215,216,217,226,227,228,229,230,231,232,233]
res_minusculo=[129,130,131,132,133,134,135,136,137,145,146,147,148,149,150,151,152,153,162,163,164,165,166,167,168,169]
numeros=[240,241,242,243,244,245,246,247,248,249]
while True:
   try:
      x=input().split()
      for c in x:
         aux=int(c,8)
         if aux==64:print(" ",end="")
         else:
            try:
               print(minusculo[res_minusculo.index(aux)],end="")
            except:
               try:
                  print(maiusculo[res_maiusculo.index(aux)],end="")
               except:
                  print(numeros.index(aux),end="")
      print()
   except EOFError:break
