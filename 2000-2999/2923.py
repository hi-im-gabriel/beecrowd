while True:
   try:
      tot,ut,warn,crit=map(int,input().split())
      if (ut*100)/tot>=crit:print("critical")
      elif (ut*100)/tot>=warn:print("warning")
      else:print("OK")
   except EOFError:break
