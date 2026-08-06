while True:
    try:
        x, y = map(int, input().split())
    except EOFError:
        break

    if x == 0 and y == 0:
        break

    print(bin(x ^ y).count("1"))
