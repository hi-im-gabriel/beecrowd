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
#n= list(map(int,input().split()))
t = int(input())
while t > 0:
    t -= 1
    f = input()
    n = ''
    k = 0
   
    while True:
        if(f[k] != '!'):
            n += f[k]
            k += 1
        else:
            n = int(n)
            k = len(f) - k
            break
   
    f = 1
    for i in range(n, 1, -k):
        f *= i
    print(f)
