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
test = 1
while True:
    n = int(input())
    if n == 0:
        break
    value = 0
    print(f'Teste {test}')
    test += 1
    for _ in range(n):
        j, z = list(map(int, input().split()))
        value += (j - z)
        print(value)
    print()
