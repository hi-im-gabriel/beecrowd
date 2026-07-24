n = int(input())
best_trail = 1
best_effort = None

for trail in range(1, n + 1):
    data = list(map(int, input().split()))
    heights = data[1:]
    forward = 0
    backward = 0

    for i in range(1, len(heights)):
        difference = heights[i] - heights[i - 1]
        if difference > 0:
            forward += difference
        else:
            backward -= difference

    effort = min(forward, backward)

    if best_effort is None or effort < best_effort:
        best_effort = effort
        best_trail = trail

print(best_trail)
