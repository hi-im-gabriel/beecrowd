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
#n= list(map(int,input().split()))
#string.split("+",2)
#import re re.sub("[^0-9]", ", string)
#string.append(input()) array
r = 'ABCDE*'
while True:
    n = int(input())
    if n == 0:
        break
    for i in range(n):
        p = -1
        l = [int(x) for x in input().split()]
        for j in range(len(l)):
            if l[j] <= 127:
                if p != -1:
                    p = 5
                    break
                p = j
        print(r[p])
