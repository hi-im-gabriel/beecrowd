#n=list(map(int,input().split()))
#s.pop() remover ultimo elemento
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfabeto
aux = 1
while True:
    n = int(input())
    if n==0:
        break
    s = [int(x) for x in input().split()]
    f = [s[x] for x in range(n) if s[x] == (x + 1)]

    print("Teste %d" % aux)
    aux += 1
    print(f[0])
    print()
