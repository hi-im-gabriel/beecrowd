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
fib = [1, 1]
while len(fib) < 100:
    fib.append(fib[-1] + fib[-2])
threebonacci = []
for f in fib:
    if '3' in str(f) or f % 3 == 0:
        threebonacci.append(f)
    if len(threebonacci) >= 60:
        break
while True:
    try:
        n = int(input())
        print(threebonacci[n - 1])
    except EOFError:
        break
