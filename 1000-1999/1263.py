#n=list(map(int,input().split()))
#string.append(input()) array
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfabeto
while True:
    try:
        c = []
        c = (input().lower()).split()
        t = 0
        y = 0
        for i, j in enumerate(c):
            c[i] = j[0]
            if c[i] == c[i-1] and y == 0:
                y = 1
                t += 1
            elif c[i] != c[i-1]:
                y = 0    
        print(t)
    except EOFError:
        break
