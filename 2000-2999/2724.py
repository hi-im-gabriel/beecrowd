g = int(input())
for g in range(g):
    p = []
    for g1 in range(int(input())):
        p.append(input().strip())
    if g != 0:
        print()
    for g1 in range(int(input())):
        e = input().strip()
        exp = False
        for i in p:
            if i in e:
                if len(i) == len(e) or e.endswith(i):
                    exp = True
                    break
                if e[e.find(i)+len(i)].isupper() and not e[e.find(i)+len(i)].isdigit():
                    exp = True
                    break
        print('Prossiga' if not exp else 'Abortar')
