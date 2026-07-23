#n=list(map(int,input().split()))
#s.pop() remover ultimo elemento
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfa

while True:
    try:
        a = []
        for i in range(int(input())):
            a.append(input().split())
            a[-1][2] = int(a[-1][2])
        a.sort(key=lambda x: (x[2], x[1], x[0]))
        for nome in a:
            print(nome[0])

    except EOFError:
        break
