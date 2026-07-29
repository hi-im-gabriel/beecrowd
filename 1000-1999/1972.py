from heapq import heappop, heappush

n, m = map(int, input().split())
labyrinth = []

for row in range(n):
    line = input()
    labyrinth.append(line)
    column = line.find("H")
    if column != -1:
        start = row * m + column
    column = line.find("E")
    if column != -1:
        target = row * m + column

infinity = 10 ** 18
distance = [infinity] * (n * m)
distance[start] = 0
queue = [(0, start)]

while queue:
    current_distance, position = heappop(queue)

    if current_distance != distance[position]:
        continue
    if position == target:
        break

    row, column = divmod(position, m)

    if row > 0:
        next_position = position - m
        cell = labyrinth[row - 1][column]
        if cell != "#":
            new_distance = current_distance + (int(cell) if cell.isdigit() else 0)
            if new_distance < distance[next_position]:
                distance[next_position] = new_distance
                heappush(queue, (new_distance, next_position))

    if row + 1 < n:
        next_position = position + m
        cell = labyrinth[row + 1][column]
        if cell != "#":
            new_distance = current_distance + (int(cell) if cell.isdigit() else 0)
            if new_distance < distance[next_position]:
                distance[next_position] = new_distance
                heappush(queue, (new_distance, next_position))

    if column > 0:
        next_position = position - 1
        cell = labyrinth[row][column - 1]
        if cell != "#":
            new_distance = current_distance + (int(cell) if cell.isdigit() else 0)
            if new_distance < distance[next_position]:
                distance[next_position] = new_distance
                heappush(queue, (new_distance, next_position))

    if column + 1 < m:
        next_position = position + 1
        cell = labyrinth[row][column + 1]
        if cell != "#":
            new_distance = current_distance + (int(cell) if cell.isdigit() else 0)
            if new_distance < distance[next_position]:
                distance[next_position] = new_distance
                heappush(queue, (new_distance, next_position))

if distance[target] == infinity:
    print("ARTSKJID")
else:
    print(distance[target])
