while True:
   try:
      s=""
      for i in range(int(input())):
         letra=chr(int(input(),2))
         s+=letra
      print(s)
   except EOFError:break
