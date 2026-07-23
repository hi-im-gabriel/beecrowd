#n=list(map(int,input().split()))
#string.append(input()) array
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfabeto
final=['N','L','S','O']
while True:
    n=int(input())
    if n==0:
        break
    s=input()
    lado=1
    for i in range(n):
        if s[i]=='D':
            lado+=1
            if lado>4:
                lado=1
        else:
            lado-=1
            if lado==0:
                lado=4
    print("%c"% (final[lado-1]))
