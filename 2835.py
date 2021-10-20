while True:
    input()
    x=sorted(list(map(int,input().split())))
    if x[0]>8:print('N');break
    aux=True
    for i in range(1,len(x)):
        if x[i]-x[i-1]>8:print('N');aux=False;break
    if aux:print('S')
    break
