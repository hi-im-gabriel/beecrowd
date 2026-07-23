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
#n= list(map(int,input().split()))
while True:
    try:
        v,t=input().split()
        v=int(v)
        t=int(t)
        print(v*2*t)
    except EOFError:
        break
