#n= list(map(int,input().split()))

import math

while True:
    n=input()
    acm=0
    if n=='0':
        break
    n=n[::-1]
    for i, j in enumerate(n):
        acm+=int(j)*int(math.factorial(i+1))
    print(acm)
