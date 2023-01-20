v = list()
for g in range(int(input())):
    v.append(str(input()))
for g in range(int(input())):
    e = str(input())
    q = 0
    for i in v:
        if i.startswith(e):
            q += 1
            if q != 1:
                if len(i) > t:
                    t = len(i)
            else:
                t = len(i)
    if q != 0:
        print(q, t)
    else:
        print(-1)
