from math import sqrt

def calculate_triangle_area(a, b, c):
    s = (a + b + c) / 2
    area = sqrt(s * (s - a) * (s - b) * (s - c))

    return area

a, b, c = map(int, input().split())

print(f"{calculate_triangle_area(a, b, c):.3f} m2")
