import string
alfa=list(string.ascii_lowercase)
while True:
   try:
      saida = ''
      for _ in range(int(input())):
         l = input().split()
         pos = len(l[0]) + 3*(len(l)-1)
         saida += alfa[pos-1]
      for n in saida:
         print(n)
   except EOFError:break
