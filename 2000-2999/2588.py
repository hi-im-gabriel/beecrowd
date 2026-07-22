while True:
    try:
        s=input()
        f=set([i for i in set(list(s)) if s.count(i)%2!=0])
        if len(f)>1:print(len(f)-1)
        else:print(0)
    except EOFError:break
