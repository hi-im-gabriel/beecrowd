while True:
    n = int(input())
    if n == 0:
        break

    graph = {}

    for _ in range(n):
        student = int(input())
        friends = list(map(int, input().split()))
        graph.setdefault(student, set()).update(friends)
        for friend in friends:
            graph.setdefault(friend, set()).add(student)

    colors = {}
    possible = True

    for student in graph:
        if student in colors:
            continue

        colors[student] = 0
        queue = [student]
        position = 0

        while position < len(queue) and possible:
            current = queue[position]
            position += 1

            for friend in graph[current]:
                if friend not in colors:
                    colors[friend] = 1 - colors[current]
                    queue.append(friend)
                elif colors[friend] == colors[current]:
                    possible = False
                    break

        if not possible:
            break

    print("SIM" if possible else "NAO")
