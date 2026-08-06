from math import hypot


def cross(origin, first, second):
    return ((first[0] - origin[0]) * (second[1] - origin[1])
            - (first[1] - origin[1]) * (second[0] - origin[0]))


while True:
    n = int(input())

    if n == 0:
        break

    points = sorted(set(tuple(map(int, input().split())) for _ in range(n)))

    lower = []
    for point in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], point) <= 0:
            lower.pop()
        lower.append(point)

    upper = []
    for point in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], point) <= 0:
            upper.pop()
        upper.append(point)

    hull = lower[:-1] + upper[:-1]
    perimeter = sum(
        hypot(hull[index][0] - hull[index - 1][0],
              hull[index][1] - hull[index - 1][1])
        for index in range(len(hull))
    )

    print(f"Tera que comprar uma fita de tamanho {perimeter:.2f}.")
