import re


values = []

while True:
    try:
        values.extend(map(int, re.findall(r"\d+", input())))
    except EOFError:
        break

position = 0

while position < len(values):
    relations = values[position]
    position += 1

    if relations == 0:
        break

    parent = list(range(1001))

    def find(person):
        while parent[person] != person:
            parent[person] = parent[parent[person]]
            person = parent[person]
        return person

    for _ in range(relations):
        first = values[position]
        second = values[position + 1]
        position += 2

        first_root = find(first)
        second_root = find(second)

        if first_root != second_root:
            parent[second_root] = first_root

    host_root = find(1)
    participants = sum(find(person) == host_root for person in range(1, 1001))
    print(participants)
