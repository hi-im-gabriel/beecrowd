#n= list(map(int,input().split()))
while True:
    try:
        h,o=input().split()
        h=int(h)
        o=int(o)
        x=h-o
        if x < 0:
            x=x*-1
        print(x)

    except EOFError:
        break
