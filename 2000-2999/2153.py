while True:
   try: 
      e = str(input())
   except EOFError: break
   i=len(e)-1
   v=[]
   while i>=0:
      if e[:i].endswith(e[i:]):v.append(e[:i])
      i-=1
   if len(v) == 0:print(e)
   else:
      v.sort()
      for j in v:print(j)
