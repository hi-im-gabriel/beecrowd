t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    weights = []

    while len(weights) < n:
        weights.extend(map(int, input().split()))

    trips = 1
    current_weight = 0

    for weight in weights:
        if current_weight + weight > m:
            trips += 1
            current_weight = weight
        else:
            current_weight += weight

    print(trips)
