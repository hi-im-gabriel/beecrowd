n = int(input())
floors = list(map(int, input().split()))

best_left = floors[0]
maximum_distance = 0

for index in range(1, n):
    maximum_distance = max(maximum_distance, floors[index] + index + best_left)
    best_left = max(best_left, floors[index] - index)

print(maximum_distance)
