t = int(input())

for _ in range(t):
    s, c, r = map(int, input().split())
    speeds = list(map(int, input().split()))
    speeds.sort()

    total_time = 0.0
    for i, speed in enumerate(speeds):
        if i < c:
            total_time += 1.0 / (speed + r)
        else:
            total_time += 1.0 / speed

    print(f"{total_time:.2f}")
