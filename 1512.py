from math import gcd

while True:
    n,a,b=map(int,input().split())
    if n==a==b==0:break
    aux = 0
    lcm = (a * b) // gcd(a, b)
    aux = n//a + n//b - n//lcm
    print(aux)
