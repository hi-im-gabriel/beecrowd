from collections import deque

while True:
    try:
        n = int(input())
    except EOFError:
        break

    graph = [[] for _ in range(n)]
    indegree = [0] * n

    for file_index in range(n):
        data = list(map(int, input().split()))
        indegree[file_index] = data[0]

        for dependency in data[1:]:
            graph[dependency - 1].append(file_index)

    queue = deque(
        file_index for file_index in range(n) if indegree[file_index] == 0
    )
    compiled = 0
    minutes = 0

    while queue:
        for _ in range(len(queue)):
            dependency = queue.popleft()
            compiled += 1

            for file_index in graph[dependency]:
                indegree[file_index] -= 1

                if indegree[file_index] == 0:
                    queue.append(file_index)

        minutes += 1

    print(minutes if compiled == n else -1)
