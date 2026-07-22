a=int(input())
b=int(input())
if a>b:a,b=b,a
for i in range(a+1,b):
    if i%5==2 or i%5==3:print(i)
