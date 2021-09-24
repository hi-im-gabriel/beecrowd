def stol(s):
    return [int(c) for c in s]
while True:
    try:
        s=stol(input())
        f=set(s)
        d=dict()
        for x in f:
            d[x]=s.count(x)
        d=dict(sorted(d.items(), key=lambda item: item[0],reverse=True))
        d=dict(sorted(d.items(), key=lambda item: item[1],reverse=True))
        for i,j in d.items():
            print(i)
            break
    except EOFError:break
