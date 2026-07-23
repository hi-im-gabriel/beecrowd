1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
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
for n in range(int(input())):
    a,b,c,d=map(int,input().split())
    taxa = float((d-b)/(c-a))
    taxa = str('%.3f' % taxa).replace('.', ',')
    taxa = taxa[:len(taxa) - 1]
    print((taxa))
