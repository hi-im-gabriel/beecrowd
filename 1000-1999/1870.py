while True:
    l, c, p = map(int, input().split())

    if l == 0 and c == 0 and p == 0:
        break

    box = [list(map(int, input().split())) for _ in range(l)]
    column = p - 1
    exploded = False

    for row_index, row in enumerate(box):
        if row[column] != 0:
            print("BOOM", row_index + 1, column + 1)
            exploded = True
            break

        left = column - 1
        while row[left] == 0:
            left -= 1

        right = column + 1
        while row[right] == 0:
            right += 1

        destination = column + row[left] - row[right]

        if destination <= left:
            print("BOOM", row_index + 1, left + 1)
            exploded = True
            break

        if destination >= right:
            print("BOOM", row_index + 1, right + 1)
            exploded = True
            break

        column = destination

    if not exploded:
        print("OUT", column + 1)
