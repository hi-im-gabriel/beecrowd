1
2
3
4
5
6
7
8
9
n = int(input())
s = list(map(int, input().split()))
total = 0
for x in s:
    total += (x // 3) * 3
print(total)
