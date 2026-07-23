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
import math
while True:
    try:
        F = float(input())
        ratio = math.sin(math.radians(108)) / math.sin(math.radians(63))
        answer = F * ratio
        print(f"{answer:.10f}")
    except EOFError:
        break
