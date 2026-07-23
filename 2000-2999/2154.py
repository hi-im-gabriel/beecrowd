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
18
19
20
21
22
23
24
25
26
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
        t = int(input())
        pol = input().split(' + ')
        der = []
        for i in pol:
            x = i.split('x')
            valor = int(x[0]) * int(x[1])
            if (int(x[1]) - 1) != 1:
                der.append(str(valor) + 'x' + str(int(x[1]) - 1))
            else:
                der.append(str(valor) + 'x')
        der = ' + '.join(der)
        print(der)
    except EOFError:
        break
