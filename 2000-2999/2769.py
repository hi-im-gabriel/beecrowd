values = []

while True:
    try:
        values.extend(map(int, input().split()))
    except EOFError:
        break

index = 0

while index < len(values):
    n = values[index]
    index += 1

    e1, e2 = values[index:index + 2]
    index += 2

    a1 = values[index:index + n]
    index += n
    a2 = values[index:index + n]
    index += n

    t1 = values[index:index + n - 1]
    index += n - 1
    t2 = values[index:index + n - 1]
    index += n - 1

    x1, x2 = values[index:index + 2]
    index += 2

    line1 = e1 + a1[0]
    line2 = e2 + a2[0]

    for stage in range(1, n):
        next_line1 = min(line1, line2 + t2[stage - 1]) + a1[stage]
        next_line2 = min(line2, line1 + t1[stage - 1]) + a2[stage]
        line1 = next_line1
        line2 = next_line2

    print(min(line1 + x1, line2 + x2))
