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
#n,m=map(int, input().split())
#n= list(map(int,input().split()))
#string.split('+',2)
#string.append(input()) stringarray
#string = string.replace(a, "")
#import re re.sub('[^0-9]', '', string)
#print(menor, end=' ')
t = int(input())
for i in range(t):
    t -= 1
    conv = input()
    r, g, b = [int(x) for x in input().split()]
    if conv == 'eye':
        p = int(r*0.30 + g*0.59 + b*0.11)
    elif conv == 'mean':
        p = int((r + g + b) / 3)
    elif conv == 'max':
        p = max(r, g, b)
    elif conv == 'min':
        p = min(r, g, b)
    print('Caso #%d: %d' % (i+1, p))
