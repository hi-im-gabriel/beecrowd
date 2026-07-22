while True:
   try:
      n,d=map(int,input().split())
      aux="0"
      temp=True
      for i in range(d):
         s=input().split()
         x=s.pop(0)
         s=list(map(int,s))
         if temp and sum(s)==len(s):
            aux=x
            temp=False
      print(aux) if aux!="0" else print("Pizza antes de FdI")
   except EOFError:break
