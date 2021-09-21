while True:
   t = int(input())
   if not t: break
   while True:
      a = [int(x) for x in input().split()]
      if len(a) == 1 and a[0] == 0:
         print()
         break
      e = []
      resp = 'No'
      n = t
      while True:
         if n == 0:
            resp = 'Yes'
            break
         if len(a) and a[-1] == n:
            a.remove(n)
            n -= 1
         elif len(e) and e[-1] == n:
            e.remove(n)
            n -= 1
         elif len(a):
            e.append(a[-1])
            a.remove(a[-1])
         else: break
      print(resp)
