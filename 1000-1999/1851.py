import heapq

dragons = []

while True:
    try:
        training_time, fine = map(int, input().split())
        dragons.append((training_time, fine))
    except EOFError:
        break

waiting = []
day = 0
next_dragon = 0
total_fine = 0

while next_dragon < len(dragons) or waiting:
    while next_dragon < len(dragons) and next_dragon <= day:
        training_time, fine = dragons[next_dragon]
        heapq.heappush(waiting, (training_time / fine, next_dragon, training_time, fine))
        next_dragon += 1

    if not waiting:
        day = next_dragon
        continue

    _, arrival_day, training_time, fine = heapq.heappop(waiting)
    total_fine += (day - arrival_day) * fine
    day += training_time

print(total_fine)
