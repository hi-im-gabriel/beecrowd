n = int(input())
s = list(map(int, input().split()))

total = 0
for x in s:
    total += (x // 3) * 3

print(total)
