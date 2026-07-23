#n=list(map(int,input().split()))
#s.pop() remover ultimo elemento
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfabeto

c = int(input())
l = int(input())

m = []
for i in range(l):
    m.append([e for e in input()])
t = False
i = j = 0
a = '!'
while True:
    if m[i][j] == '.': m[i][j] = a
    if m[i][j] == '*':
        t = True
        break
    elif m[i][j] == '!': break
    elif m[i][j] == '>':
        if j < c-1:
            a = '>'
            m[i][j] = '!'
            j += 1
        else: break
    elif m[i][j] == '<':
        if 0 < j:
            a = '<'
            m[i][j] = '!'
            j -= 1
        else: break
    elif m[i][j] == '^':
        if 0 < i:
            a = '^'
            m[i][j] = '!'
            i -= 1
        else: break
    elif m[i][j] == 'v':
        if i < l-1:
            a = 'v'
            m[i][j] = '!'
            i += 1
        else: break
print(m[i][j])
