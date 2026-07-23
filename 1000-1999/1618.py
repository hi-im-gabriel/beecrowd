#n=list(map(int,input().split()))
#s.pop() remover ultimo elemento
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfa

for i in range(int(input())):
    e = [int(x) for x in str(input()).split()]
    ax = e[0]
    ay = e[1]
    bx = e[2]
    by = e[3]
    cx = e[4]
    cy = e[5]
    dx = e[6]
    dy = e[7]
    rx = e[8]
    ry = e[9]
    if dy >= ry and cy >= ry and ay <= ry and by <= ry:
        if dx <= rx and ax <= rx and cx >= rx and bx >= rx:
            print(1)
        else: print(0)
    else: print(0)
