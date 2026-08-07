from bisect import bisect_left, bisect_right

fibonacci = [1, 2]

while fibonacci[-1] <= 10 ** 100:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])

while True:
    a, b = map(int, input().split())

    if a == 0 and b == 0:
        break

    print(bisect_right(fibonacci, b) - bisect_left(fibonacci, a))
