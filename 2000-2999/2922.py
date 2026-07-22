while True:
    try:
        a,b=map(int,input().split())
        if a>b:a,b=b,a
        if a==b:print(b-a)
        else:print(b-a-1)
    except EOFError:break
