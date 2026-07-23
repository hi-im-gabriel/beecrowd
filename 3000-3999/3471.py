1
2
3
4
5
6
7
import math
n, m = map(int, input().split())
g = math.gcd(n, m)
print(1 if g == 1 else g)
