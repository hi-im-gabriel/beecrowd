n, c, s = map(int, input().split())
commands = list(map(int, input().split()))

position = 1
visits = 1 if position == s else 0

for command in commands:
    position = (position - 1 + command) % n + 1
    if position == s:
        visits += 1

print(visits)
