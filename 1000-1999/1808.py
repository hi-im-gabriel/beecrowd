#n=list(map(int,input().split()))
#s.pop() remover ultimo elemento
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfabeto

e = input()
s=q=0
while len(e) > 0:
    if e[-1] != '0':
        s += int(e[-1])
        e = e[:len(e)-1]
    else:
        s += 10
        e = e[:len(e)-2]
    q += 1
print("%.2f"%float(s/q))
