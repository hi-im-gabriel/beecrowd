while True:
    try:
        a,b=map(int,input().split())
        c=a^b
        print(c)
    except EOFError:break
