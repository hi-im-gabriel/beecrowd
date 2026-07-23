#n= list(map(int,input().split()))
n=int(input())

while n>=1:
    x=int(input())
    print("%d kg" % ((pow(2,x))/12000))

    n-=1
