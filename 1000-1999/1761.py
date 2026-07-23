#n= list(map(int,input().split()))
#string.split("+",2)
#import re re.sub("[^0-9]", ", string)
#string.append(input()) array
#s=sorted(s,key=len,reverse=True)
#print(*s,sep=" ")
from math import tan

while True:
    try:
        a,b,c=map(float,input().split())
        angulo=tan((a*3.141592654)/180.00)
        dist=b*angulo
        res=(dist+c)*5

        print("%.2f"%(res))
    except EOFError:
        break
