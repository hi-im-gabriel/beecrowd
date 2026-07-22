for _ in range(int(input())):
    f = []
    for _ in range(int(input())):
        s = input().split()
        if s[1] == 'chirrin' and s[0] not in f:f.append(s[0])
        elif s[1] == 'chirrion' and s[0] in f:f.remove(s[0])
    f.sort()
    print('TOTAL')
    print(*f,sep="\n")
