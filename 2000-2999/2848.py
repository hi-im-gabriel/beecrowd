n, q = map(int, input().split())
numbers = list(map(int, input().split()))

for _ in range(q):
    l, r, k, g, d = map(int, input().split())
    interval = sorted(numbers[l - 1:r])
    value = interval[k - 1]
    frequency = interval.count(value)

    g_difference = abs(g - frequency)
    d_difference = abs(d - frequency)

    if g_difference < d_difference:
        winner = "G"
    elif d_difference < g_difference:
        winner = "D"
    else:
        winner = "E"

    print(value, frequency, winner)
