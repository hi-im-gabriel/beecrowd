from math import gcd as helloworld
while True:
    try:
        n=int(input())
        l=list(map(int,input().split()))
        aux=l[0]
        for i in l[1:]:aux=((aux*i)//(helloworld(aux,i)))
        aux-=n
        print(aux)
    except EOFError:break
