while True:
    try:
        n=int(input())
        if n==0:break
        a=list(map(int,input().split()))
        b=set()
        [b.remove(x) if x in b else b.add(x) for x in a]        
        print(list(b)[0])
    except:break
