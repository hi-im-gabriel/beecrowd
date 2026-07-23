#n= list(map(int,input().split()))
#string.split('+',2)
#string.append(input())
#string = string.replace(a, "")
#import re re.sub('[^0-9]', '', string)

a=int(input())
b=int(input())
c=int(input())

x1=a*0+b*2+c*4
x2=a*2+b*0+c*2
x3=a*4+b*2+c*0

if x1<=x2:
    result=x1
else:
    result=x2
if result>=x3:
    result=x3
print(result)
