while True:
    try:
        m, n = map(int, input().split())
    except EOFError:
        break

    total = 0
    for _ in range(m):
        total += sum(map(int, input().split()))

    print(f"{total // 60} saca(s) e {total % 60} litro(s)")
