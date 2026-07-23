1
2
3
4
5
6
7
8
9
10
11
12
13
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
