largest = 0
n = int(input())
v = [0] * (n + 2)

v[0] = 0
v[n + 1] = 0
tmp_list = list(map(int, input().split()))
for i in range(1, n + 1):
    v[i] = tmp_list[i - 1]
    if v[i] > v[i - 1]:
        v[i] = v[i - 1] + 1

for i in range(n, 0, -1):
    if v[i] > v[i + 1]:
        v[i] = v[i + 1] + 1

for i in range(n + 2):
    if v[i] > largest:
        largest = v[i]

print(largest)
