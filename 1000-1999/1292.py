import math

while True:
    try:
        F = float(input())
        ratio = math.sin(math.radians(108)) / math.sin(math.radians(63))
        answer = F * ratio
        print(f"{answer:.10f}")
    except EOFError:
        break
