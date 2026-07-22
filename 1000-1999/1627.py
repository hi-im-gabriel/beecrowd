for _ in range(int(input())):
    at,ad,bt,bd=map(int,input().split())
    h=int(input())
    ra=rb=0
    while True:
        if ra<=rb:
            h-=at
            rb-=ra
            ra=ad
            if h<=0:print('Andre');break
        else:
            h-=bt
            ra-=rb
            rb=bd
            if h<=0:print('Beto');break
