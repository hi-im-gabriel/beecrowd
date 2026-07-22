from itertools import permutations as permu
for _ in range(int(input())):
    f=[]
    s=input()
    for c in permu(s):
        p = list(c)
        f.append(''.join(p))
    f=list(dict.fromkeys(f))
    f.sort()
    print(*f,sep="\n")
    print()
