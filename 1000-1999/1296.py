1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
from math import sqrt
while True:
    try:
        m1, m2, m3 = map(float, input().split())
        sm = (m1 + m2 + m3) / 2.0
        try:
            area = 4 * sqrt(sm * (sm - m1) * (sm - m2) * (sm - m3)) / 3.0
        except ValueError:
            area = -1.0
        if area == 0:
            area = -1.0
        print(f"{area:.3f}")
    except EOFError:
        break
