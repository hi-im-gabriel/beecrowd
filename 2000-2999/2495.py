while True:
    try:
        n = int(input())
    except EOFError:
        break

    missing = n * (n + 1) // 2
    returned = 0

    while returned < n - 1:
        pens = list(map(int, input().split()))
        missing -= sum(pens)
        returned += len(pens)

    print(missing)
