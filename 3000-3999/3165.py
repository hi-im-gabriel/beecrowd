#n= list(map(int,input().split()))
#string.split("+",2)
#import re re.sub("[^0-9]", ", string)
#string.append(input()) array
#s=sorted(s,key=len,reverse=True)
#print(*s,sep=" ")

from math import sqrt

def primo(n):
    if n<2:
        return False
    i=2
    while i<=sqrt(n):
        if n%i==0 and n!=i:
            return False
        i+=1
    return True

n=int(input())

if n%2==0:
    n-=1

i=n
aux=0
aux2=0
while i>=5:
    if primo(i):
        if primo(i-2):
            aux=i-2
            aux2=i
            break

    i-=2
print("%d %d" % (aux,aux2))
