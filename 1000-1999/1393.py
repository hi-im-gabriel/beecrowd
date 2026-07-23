#n= list(map(int,input().split()))

from math import sqrt

while True:
    n=float(input())
    if n==0:
        break
    zero=0.0
    um=1.0
    aux=0
    i=1
    while i <= int(n):
        aux=zero+um
        zero=um
        um=aux
        i+=1
    print("%d" % (aux))
