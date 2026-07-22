for _ in range(int(input())):
   x,y=map(int,input().split('x'))
   
   for i in range(5,11):
      print(f"{x} x {i} = {x*i}") if x==y else print(f"{x} x {i} = {x*i} && {y} x {i} = {y*i}")
