n = int(input())
count = 0
for i in range(n):
    c, p = map(int, input().split())
    count += c / p
if count > 1:
    print("FAIL")
else:
    print("OK")
