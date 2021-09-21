n=int(input())
p=list(map(int,input().split()))
m=int(input())
sairam=list(map(int,input().split()))

for i in sairam:
   p.remove(i)
print(*p,sep=" ")
