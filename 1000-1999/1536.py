#n=list(map(int,input().split()))
#s.pop() remover ultimo elemento
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfabeto

q = int(input())
for p in range(q):
    s1 = s2 = p1 = p2 = a1 = a2 = 0
    e = str(input()).split()
    a = int(e[0])
    b = int(e[2])
    a2 = a
    s1 += a
    s2 += b
    if a > b: p1 += 3
    elif b > a: p2 += 3
    else:
        p1 += 1
        p2 += 1
    e = str(input()).split()
    b = int(e[0])
    a = int(e[2])
    a1 = b
    s1 += a
    s2 += b
    if a > b: p1 += 3
    elif b > a: p2 += 3
    else:
        p1 += 1
        p2 += 1
    if p1 > p2:print("Time 1")
    elif p2 > p1:print("Time 2")
    else:
        if s1 - s2 > s2 - s1: print("Time 1")
        elif s2 - s1 > s1 - s2: print("Time 2")
        else:
            if a1 > a2: print("Time 1")
            elif a2 > a1: print("Time 2")
            else: print("Penaltis")
