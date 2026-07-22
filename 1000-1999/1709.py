p=int(input())
a,b=2,1
while a!=1:
    if a<=int(p/2):a+=a
    else:a-=(p-a+1)
    b+=1
print(b)
