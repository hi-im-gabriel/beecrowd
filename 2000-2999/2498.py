case_number = 1

while True:
    n, capacity = map(int, input().split())

    if n == 0 and capacity == 0:
        break

    maximum_interest = [0] * (capacity + 1)

    for _ in range(n):
        weight, interest = map(int, input().split())

        for current_capacity in range(capacity, weight - 1, -1):
            maximum_interest[current_capacity] = max(
                maximum_interest[current_capacity],
                maximum_interest[current_capacity - weight] + interest,
            )

    print(f"Caso {case_number}: {maximum_interest[capacity]}")
    case_number += 1
