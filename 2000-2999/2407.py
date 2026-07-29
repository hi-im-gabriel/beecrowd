n = int(input())

seen = [False] * (n * n + 1)
column_sums = [0] * n
magic_value = None
main_diagonal = 0
secondary_diagonal = 0
valid = True

for i in range(n):
    row = list(map(int, input().split()))
    row_sum = 0

    for j, value in enumerate(row):
        row_sum += value
        column_sums[j] += value

        if value < 1 or value > n * n or seen[value]:
            valid = False
        else:
            seen[value] = True

        if i == j:
            main_diagonal += value
        if i + j == n - 1:
            secondary_diagonal += value

    if magic_value is None:
        magic_value = row_sum
    elif row_sum != magic_value:
        valid = False

if any(total != magic_value for total in column_sums):
    valid = False

if main_diagonal != magic_value or secondary_diagonal != magic_value:
    valid = False

print(magic_value if valid else 0)
