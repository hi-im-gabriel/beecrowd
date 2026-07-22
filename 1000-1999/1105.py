while True:
    b,n=input().split()
    if b==n=='0':break
    r = list(map(int,input().split()))
    for i in range(int(n)):
        d, c, v = input().split()
        r[int(d)-1] -= int(v)
        r[int(c)-1] += int(v)
    aux = 'S'
    for i in r:
        if int(i) < 0:
            aux = 'N'
            break
    print(aux)
