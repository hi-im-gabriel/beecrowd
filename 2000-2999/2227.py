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
test = 1
while True:
    a, v = list(map(int, input().split()))
    if a == v == 0:
        break
    temp = [0] * a
    for _ in range(v):
        x, y =  list(map(int, input().split()))
        temp[x-1] += 1
        temp[y-1] += 1
    m = max(temp)
    bigger = [str(i + 1) for i in range(len(temp)) if temp[i] == m]
    print(f'Teste {test}')
    test += 1
    print(' '.join(bigger), '')
    print()
