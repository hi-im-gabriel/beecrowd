n = int(input())
rows = [input().strip() for _ in range(n)]

group_ids = {}
person_group = []
sizes = []

for row in rows:
    if row not in group_ids:
        group_ids[row] = len(sizes)
        sizes.append(0)
    group = group_ids[row]
    person_group.append(group)
    sizes[group] += 1

consistent = True

for i in range(n):
    for j in range(n):
        if (rows[i][j] == 'S') != (person_group[i] == person_group[j]):
            consistent = False
            break
    if not consistent:
        break

if not consistent:
    print(-1)
else:
    sizes.sort(reverse=True)
    print(len(sizes))
    print(*sizes)
