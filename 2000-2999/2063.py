from math import gcd

n = int(input())
tunnels = list(map(int, input().split()))

answer = 1
visited = [False] * n

for start in range(n):
    if not visited[start]:
        current = start
        cycle_length = 0

        while not visited[current]:
            visited[current] = True
            cycle_length += 1
            current = tunnels[current] - 1

        answer = answer * cycle_length // gcd(answer, cycle_length)

print(answer)
