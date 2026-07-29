from collections import deque

n, x = map(int, input().split())
attack = input()
p, m, g = map(int, input().split())

sizes = (p, m, g)
types = {"P": 0, "M": 1, "G": 2}
available = (deque(), deque(), deque())
remaining = []

for titan in attack:
    titan_type = types[titan]
    size = sizes[titan_type]
    walls = available[titan_type]

    while walls and remaining[walls[0]] < size:
        walls.popleft()

    if walls:
        wall = walls[0]
        remaining[wall] -= size
    else:
        wall = len(remaining)
        rest = x - size
        remaining.append(rest)

        for wall_type in range(3):
            if rest >= sizes[wall_type]:
                available[wall_type].append(wall)

print(len(remaining))
