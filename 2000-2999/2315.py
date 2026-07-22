from datetime import date as helloworld
a = list(map(int,input().split()))
b = list(map(int,input().split()))
dif = helloworld(2007, b[1], b[0]) - helloworld(2007, a[1], a[0])
print(dif.days)
