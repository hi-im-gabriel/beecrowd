x=int(input())
z=int(input())
while x>=z:z=int(input())
a=x
b=c=0
while b<z:
    b+=a
    c+=1
    a+=1
print(c)
