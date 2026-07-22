for i in range(int(input())):
    x=int(input())
    if x==0:print("NULL")
    elif x<=0:
        x*=-1
        if x%2==0:print("EVEN NEGATIVE")
        else:print("ODD NEGATIVE")
    else:
        if x%2==0:print("EVEN POSITIVE")
        else:print("ODD POSITIVE")
