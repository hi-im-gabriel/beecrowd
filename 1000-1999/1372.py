while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break

    previous_rows = 0
    best_rows = 0

    for _ in range(m):
        candies = map(int, input().split())
        previous_columns = 0
        best_columns = 0

        for candy in candies:
            previous_columns, best_columns = best_columns, max(
                best_columns, previous_columns + candy
            )

        previous_rows, best_rows = best_rows, max(
            best_rows, previous_rows + best_columns
        )

    print(best_rows)
