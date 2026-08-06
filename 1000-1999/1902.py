loves = {}

while True:
    try:
        data = input().split()
    except EOFError:
        break

    if data:
        loves[data[0]] = data[1]

state = {}
answer = 0

for person in loves:
    if state.get(person, 0) != 0:
        continue

    current = person
    path = []

    while current in loves and state.get(current, 0) == 0:
        state[current] = 1
        path.append(current)
        current = loves[current]

    if state.get(current, 0) == 1:
        cycle_size = 1
        next_person = loves[current]

        while next_person != current:
            cycle_size += 1
            next_person = loves[next_person]

        if cycle_size >= 2:
            answer += 1

    for visited in path:
        state[visited] = 2

print(answer)
