while True:
    n = int(input())
    if n == 0:break
    cont = 0
    while True:
        m = list(map(int,input().split()))
        if m == sorted(m):
            cont += 1
            print(cont)
            break
        else:cont += 1
