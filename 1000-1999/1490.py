while True:
    try:
        n = int(input())
    except EOFError:
        break

    board = [input() for _ in range(n)]
    horizontal = [[-1] * n for _ in range(n)]
    vertical = [[-1] * n for _ in range(n)]

    horizontal_count = 0
    for i in range(n):
        active = False
        for j in range(n):
            if board[i][j] == "X":
                active = False
            else:
                if not active:
                    horizontal_count += 1
                    active = True
                horizontal[i][j] = horizontal_count - 1

    vertical_count = 0
    for j in range(n):
        active = False
        for i in range(n):
            if board[i][j] == "X":
                active = False
            else:
                if not active:
                    vertical_count += 1
                    active = True
                vertical[i][j] = vertical_count - 1

    graph = [[] for _ in range(horizontal_count)]
    for i in range(n):
        for j in range(n):
            if board[i][j] == ".":
                graph[horizontal[i][j]].append(vertical[i][j])

    matched_horizontal = [-1] * horizontal_count
    matched_vertical = [-1] * vertical_count

    def augment(start):
        visited_horizontal = [False] * horizontal_count
        visited_vertical = [False] * vertical_count
        parent_vertical = [-1] * vertical_count
        stack = [start]
        visited_horizontal[start] = True

        while stack:
            horizontal_segment = stack.pop()
            for vertical_segment in graph[horizontal_segment]:
                if visited_vertical[vertical_segment]:
                    continue

                visited_vertical[vertical_segment] = True
                parent_vertical[vertical_segment] = horizontal_segment

                if matched_vertical[vertical_segment] == -1:
                    while vertical_segment != -1:
                        horizontal_segment = parent_vertical[vertical_segment]
                        previous_vertical = matched_horizontal[horizontal_segment]
                        matched_horizontal[horizontal_segment] = vertical_segment
                        matched_vertical[vertical_segment] = horizontal_segment
                        vertical_segment = previous_vertical
                    return True

                next_horizontal = matched_vertical[vertical_segment]
                if not visited_horizontal[next_horizontal]:
                    visited_horizontal[next_horizontal] = True
                    stack.append(next_horizontal)

        return False

    answer = 0
    for horizontal_segment in range(horizontal_count):
        if augment(horizontal_segment):
            answer += 1

    print(answer)
