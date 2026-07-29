while True:
    n, m = map(int, input().split())

    if n == -1 and m == -1:
        break

    chapters = list(map(int, input().split()))
    total = sum(chapters[i] * (n - i) for i in range(n))
    print(total * m)
