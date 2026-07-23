#n=list(map(int,input().split()))
#s.pop() remover ultimo elemento
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa = list(string.ascii_lowercase) lsit do alfa
#d=dict()
#d[key]=s[value]
#d=dict(sorted(d.items(), key=lambda item: item[1]))

while (True):
    stick_sizes = int(input())
    sum_aux = 0
    if (not stick_sizes):
        break
    for i in range(stick_sizes):
        line = int(input().split()[1])
        if (line % 2 == 0):
            sum_aux += line
            continue
        sum_aux += line - 1                
    print(int(sum_aux/4))
