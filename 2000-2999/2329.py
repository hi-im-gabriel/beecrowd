n = int(input())
k = int(input())
sizes = list(map(int, input().split()))

low = 1
high = max(sizes)
answer = 0

while low <= high:
    middle = (low + high) // 2
    pieces = sum(size // middle for size in sizes)

    if pieces >= n:
        answer = middle
        low = middle + 1
    else:
        high = middle - 1

print(answer)
