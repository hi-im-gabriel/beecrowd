#n= list(map(int,input().split()))
#string.append(input()) array
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfabeto


for i in range(int(input())):
    l = list(map(int, input().split()))
    m = l[0]
    sum ,c = 0, 0
    for i in range(1, len(l)):
        sum += l[i]
    for e in range(1, len(l)):
        if l[e] > (sum/m):
            c += 1
    print("%.3f" % (c*100/m) + '%')
