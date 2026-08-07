while True:
    n, p = map(int, input().split())

    if n == 0 and p == 0:
        break

    heights = []
    target_stack = 0
    target_level = 0

    for i in range(p):
        values = list(map(int, input().split()))
        boxes = values[1:]
        heights.append(values[0])

        if 1 in boxes:
            target_stack = i
            target_level = boxes.index(1)

    left_cost = 0
    i = target_stack - 1
    while i >= 0 and heights[i] > target_level:
        left_cost += heights[i] - target_level
        i -= 1

    right_cost = 0
    i = target_stack + 1
    while i < p and heights[i] > target_level:
        right_cost += heights[i] - target_level
        i += 1

    boxes_above = heights[target_stack] - target_level - 1
    print(boxes_above + min(left_cost, right_cost))
