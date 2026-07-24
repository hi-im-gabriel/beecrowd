while True:
    try:
        n, h = map(int, input().split())
    except EOFError:
        break

    tasks = []
    total = 0

    for _ in range(n):
        value, deadline = map(int, input().split())
        tasks.append((value, deadline))
        total += value

    tasks.sort(reverse=True)

    parent = list(range(h + 1))

    def find(hour):
        while parent[hour] != hour:
            parent[hour] = parent[parent[hour]]
            hour = parent[hour]
        return hour

    earned = 0

    for value, deadline in tasks:
        hour = find(deadline)
        if hour > 0:
            earned += value
            parent[hour] = find(hour - 1)

    print(total - earned)
