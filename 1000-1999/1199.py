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
#n= list(map(int,input().split()))
while True:
    n = input()
    if n == '-1':
        break
    if n.isdigit():
        n = hex(int(n))
        n = n[:2] + n[2:].upper()
    else:
        n = int(n,16)
    print(n)
