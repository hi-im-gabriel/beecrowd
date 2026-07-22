while True:
   try:

      aux=0
      for i in range(int(input())):
         especie=input().split()
         raca=input().split()
         nome=input().split()
         input()
         if especie[0]=="cachorro" and len(nome)>1:
            for j in range(len(nome)):
               if nome[j][0]==raca[0][0]:
                  aux+=1
                  break
      print(aux)
   except EOFError:break
