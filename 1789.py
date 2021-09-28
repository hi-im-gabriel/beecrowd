while True:
    try:
        int(input())
        x=list(map(int,input().split()))
        if max(x)<10:print(1)
        elif max(x)>=10 and max(x)<20:print(2)
        else:print(3)
    except EOFError:break
