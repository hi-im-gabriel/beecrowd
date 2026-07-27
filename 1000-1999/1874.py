while True:
    try:
        H, P, F = map(int, input().split())
    except EOFError:
        break

    if H == 0 and P == 0 and F == 0:
        break

    stacks = [list(map(int, input().split())) for _ in range(H)]
    blocks = list(map(int, input().split()))
    block_index = 0

    for column in range(P - 1, -1, -1):
        for row in range(H - 1, -1, -1):
            if stacks[row][column] == 0:
                if block_index == F:
                    break
                stacks[row][column] = blocks[block_index]
                block_index += 1
        if block_index == F:
            break

    for row in stacks:
        print(*row)
