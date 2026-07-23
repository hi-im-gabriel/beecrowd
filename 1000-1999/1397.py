#n= list(map(int,input().split()))
#string.split("+",2)
#import re re.sub("[^0-9]", ", string)
#string.append(input()) array

while True:
    n=int(input())
    j1=j2=0
    if n==0:
        break
    while n:
        a,b=input().split()
        a=int(a)
        b=int(b)
        if a>b:
            j1+=1
        elif b>a:
            j2+=1

        n-=1
    print("%d %d" % (j1,j2))
