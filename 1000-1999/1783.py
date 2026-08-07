def calcula(p1, p2, p3, p4):
    a1 = 2 * (p2[0] - p1[0])
    b1 = 2 * (p2[1] - p1[1])
    c1 = (
        p1[0] ** 2 - p2[0] ** 2
        + p1[1] ** 2 - p2[1] ** 2
    )

    a2 = 2 * (p4[0] - p3[0])
    b2 = 2 * (p4[1] - p3[1])
    c2 = (
        p3[0] ** 2 - p4[0] ** 2
        + p3[1] ** 2 - p4[1] ** 2
    )

    det = a1 * b2 - a2 * b1

    if abs(det) < 1e-12:
        return 0.0, 0.0

    x = (c1 * b2 - c2 * b1) / det
    y = (a1 * c2 - a2 * c1) / det

    return -x, -y


t = int(input())

for case in range(1, t + 1):
    a1 = tuple(map(float, input().split()))
    a2 = tuple(map(float, input().split()))
    n1 = tuple(map(float, input().split()))
    n2 = tuple(map(float, input().split()))

    x, y = calcula(a1, n1, a2, n2)

    if abs(x) < 0.0005:
        x = 0.0

    if abs(y) < 0.0005:
        y = 0.0

    print(f"Caso #{case}: {x:.2f} {y:.2f}")
