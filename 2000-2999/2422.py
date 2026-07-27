n = int(input())
houses = [int(input()) for _ in range(n)]
k = int(input())

left = 0
right = n - 1

while left < right:
    total = houses[left] + houses[right]

    if total == k:
        print(houses[left], houses[right])
        break
    if total < k:
        left += 1
    else:
        right -= 1
