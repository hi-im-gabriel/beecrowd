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
#n= list(map(int,input().split()))
#string.split('+',2)
#string.append(input())
#string = string.replace(a, "")
#import re re.sub('[^0-9]', '', string)
while True:
    try:
        n, q = [int(x) for x in input().split()]
        cid = []
        while n:
            n -= 1
            cid.append(int(input()))
        cid.sort(reverse=True)
        while q:
            q -= 1
            p = input()
            print(cid[int(p) - 1])
    except EOFError:
        break
