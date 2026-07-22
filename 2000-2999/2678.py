import string
alfa=list(string.ascii_uppercase)
conv=[2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,7,8,8,8,9,9,9,9]
while True:
   try:
      s=input()
      f=""
      for c in s:
         if c.isnumeric():
            f+=c
            
         elif c.isalpha():
            f+=str(conv[alfa.index(c.upper())])
         else:
            if c=='*' or c=='#':
               f+=c
      print(f)
   except EOFError:break
