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
while True:
    n = int(input())
    if n == 0:
        break
    
    ans = 0
    over = 0
    costs = list(map(int, input().split()))
    for cost in costs:
        over += cost
        ans += abs(over)
    
    print(ans)
