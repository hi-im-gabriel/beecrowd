a=int(input())
b=int(input())
if a>b:a,b=b,a
soma=0
for i in range(a,b+1):
    if i%13!=0:soma+=i
print(soma)
