while True:
    try:
        a,b,c= list(map(int,input().split()))
        if a==b==c:print("*")
        else:
            if a==b:print("C")
            else:
                print("B") if a==c else print("A")
    except EOFError:break
