from math import pi, sqrt

while True:
    try:
        l = float(input())
        b = (- l) * l * (3 * (sqrt(3) - 4) + 2 * pi) / 3
        e = 4 * (l * l * (1 - pi/4) - (b) / 2)
        c = l * l - e - b
        print(f'{c:.3f} {e:.3f} {b:.3f}')
    except EOFError:
        break
