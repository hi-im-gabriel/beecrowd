from math import pi


c = int(input())

for _ in range(c):
    n, liters = map(int, input().split())
    b, B, H = map(int, input().split())
    target = liters / n

    low = 0.0
    high = float(H)

    for _ in range(100):
        h = (low + high) / 2
        radius = b + (B - b) * h / H
        volume = pi * h * (b * b + b * radius + radius * radius) / 3

        if volume < target:
            low = h
        else:
            high = h

    print(f"{(low + high) / 2:.2f}")
