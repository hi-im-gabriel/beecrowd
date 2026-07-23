#n= list(map(int,input().split()))
#string.append(input()) array
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfabeto

s = input().split()
for i in range(len(s)):
    if len(s[i]) > 3:
        if s[i][0:1] == s[i][2:3]:
            s[i] = s[i][2:]
s = ' '.join(s)
print(s)
