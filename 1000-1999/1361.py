p = int(input())

for _ in range(p):
    n = int(input())
    floors = [int(input()) for _ in range(n)]
    floors.sort(key=abs)

    height = 0
    last_color = 0

    for floor in floors:
        color = 1 if floor > 0 else -1
        if color != last_color:
            height += 1
            last_color = color

    print(height)
