def res(s):
    return [ord(c) for c in s]
aux=False
while True:
    try:
        s=res(input())
        x=set(s)
        d=dict()
        for c in x:
            d[c]=s.count(c)
        d=dict(sorted(d.items(),key=lambda item: (item[0]),reverse=True))
        d=dict(sorted(d.items(),key=lambda item: (item[1])))
        if aux:print()
        for i,j in d.items():
            print(i,j)
        aux=True
    except EOFError:break
