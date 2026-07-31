n, f = map(int, input().split())
cycles = list(map(int, input().split()))

left = 1
right = 100000000

while left < right:
    middle = (left + right) // 2
    coins = 0

    for cycle in cycles:
        coins += middle // cycle
        if coins >= f:
            break

    if coins >= f:
        right = middle
    else:
        left = middle + 1

print(left)
