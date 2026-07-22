while True:
    try:
        a,b,c=map(int,input().split())
    except:break
    x=int(pow((a*b*100)/c,.5))
    print(x)
