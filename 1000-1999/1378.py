from collections import Counter

while True:
    n = int(input())

    if n == 0:
        break

    points = [tuple(map(int, input().split())) for _ in range(n)]
    answer = 0

    for x1, y1 in points:
        distances = [
            (dx := x1 - x2) * dx + (dy := y1 - y2) * dy
            for x2, y2 in points
        ]
        repeated = n - len(set(distances))

        if repeated < 2:
            answer += repeated
        else:
            frequencies = Counter(distances)
            answer += sum(
                count * (count - 1) // 2
                for count in frequencies.values()
            )

    print(answer)
