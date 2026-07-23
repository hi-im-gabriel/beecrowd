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
#n= list(map(int,input().split()))
#string.split('+',2)
#string.append(input()) stringarray
#string = string.replace(a, "")
#import re re.sub('[^0-9]', '', string)
c = {'suco de laranja':120, 'morango fresco':85, 'mamao':85, 'goiaba vermelha':70, 'manga': 56, 'laranja':50, 'brocolis':34}
while True:
    n = int(input())
    if n == 0:
        break
    vitamina = 0
    for i in range(n):
        w = input().split()
        qt = int(w[0])
        fruta = ' '.join(w[1:])
        vitamina += c[fruta]*qt
    if vitamina < 110:
        print('Mais %d mg' % (110-vitamina))
    elif vitamina > 130:
        print('Menos %d mg' % (vitamina-130))
    else:
        print('%d mg' % (vitamina))
