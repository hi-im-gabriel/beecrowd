from math import gcd
a,b,c,d = map(int,input().split())
p = ((((b*d)//gcd(b,d))*a)//b)+((((b*d)//gcd(b,d))*c)//d)
q = gcd(((b*d)//gcd(b,d)),p)
print(p//q,((b*d)//gcd(b,d))//q)
