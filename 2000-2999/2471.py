n = int(input())
square = [list(map(int, input().split())) for _ in range(n)]

row_sums = [sum(row) for row in square]
column_sums = [sum(square[i][j] for i in range(n)) for j in range(n)]

magic_sum = max(set(row_sums), key=row_sums.count)
changed_row = next(i for i in range(n) if row_sums[i] != magic_sum)
changed_column = next(j for j in range(n) if column_sums[j] != magic_sum)

placed = square[changed_row][changed_column]
original = placed + magic_sum - row_sums[changed_row]

print(original, placed)
