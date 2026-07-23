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
        s, va, vb = input().split()
        if(int(va) <= int(vb)):
            print('impossivel')
        else:
            t = int(s)/(int(va)-int(vb))
            print('%.2f' % t)
    except EOFError:
        break
