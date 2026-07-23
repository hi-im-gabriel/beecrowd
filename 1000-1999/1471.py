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
        n, r = input().split()
        m = [x for x in range(1, int(n)+1)]
        l = [int(x) for x in input().split()]
        s = [x for x in m if x not in l]
        if s == []:
            s = '*'
        if s != '*':
            for x in range(len(s)):
                print(s[x], end=" ")
            print("")
        else:
            print(s) 
    except EOFError:
        break
