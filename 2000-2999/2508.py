import string
alfa=list(string.ascii_lowercase)
def strtolist(n):
   return [int(c) for c in n]
def res(s):
   soma=0
   for c in s:
      if c>='j' and c<='r':aux=alfa.index(c)-9+1
      elif c>='s' and c<='z':aux=alfa.index(c)-18+1
      elif c>='a' and c<='i':aux=alfa.index(c)+1
      else:aux=0
      soma+=aux
   return soma
def ateum(n):
   while len(n)>1:
      n=strtolist(n)
      n=str(sum(n))
   return n
while True:
   try:
      s=input().lower()
      n=str(res(s))
      n=ateum(n)
      print(n)
   except EOFError:break
