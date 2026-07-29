from collections import deque

n, G = map(int, input().split())
graph = {}

for _ in range(n):
    s, t = input().split()
    graph.setdefault(s, []).append(t)
    graph.setdefault(t, []).append(s)

visited = {"Rerisson"}
queue = deque([("Rerisson", 0)])
guests = []

while queue:
    person, distance = queue.popleft()

    if distance == G:
        continue

    for friend in graph.get(person, []):
        if friend not in visited:
            visited.add(friend)
            guests.append(friend)
            queue.append((friend, distance + 1))

guests.sort()
print(len(guests))
for guest in guests:
    print(guest)
