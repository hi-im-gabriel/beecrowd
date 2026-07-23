#n= list(map(int,input().split()))
while True:
    try:
        v,t=input().split()
        v=int(v)
        t=int(t)
        print(v*2*t)

    except EOFError:
        break
